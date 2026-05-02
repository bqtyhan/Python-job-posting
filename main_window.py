from PySide6.QtWidgets import QMainWindow
from auth_manager import AuthManager
from ui_main_window import Ui_MainWindow

# Sayfalar
from login_screen import LoginScreen
from register_screen import RegisterScreen
from job_listing_screen import JobListingScreen
from job_detail_screen import JobDetailScreen
from application_screen import ApplicationScreen
from employer_dashboard import EmployerDashboard
from admin_panel import AdminPanel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("İş İlan Sistemi")

        # UI Nesneleri
        self.sidebar = self.ui.left_menu_frame
        self.stack = self.ui.main_pages

        # Buton Bağlantıları (Tek Seferlik)
        self.ui.btn_jobs.clicked.connect(lambda: self.switch_page(JobListingScreen))
        self.ui.btn_apps.clicked.connect(lambda: self.switch_page(ApplicationScreen))
        self.ui.btn_employer.clicked.connect(lambda: self.switch_page(EmployerDashboard))
        self.ui.btn_admin.clicked.connect(lambda: self.switch_page(AdminPanel))
        self.ui.btn_logout.clicked.connect(self.logout)

        self.show_auth()

    def switch_page(self, screen_class, *args):
        while self.stack.count():
            self.stack.removeWidget(self.stack.widget(0))

        screen = screen_class(*args)

        # 🔥 LOGIN → REGISTER
        if isinstance(screen, LoginScreen):
            screen.go_register.connect(lambda: self.switch_page(RegisterScreen))
            screen.login_success.connect(self.after_login)

        # 🔥 REGISTER → LOGIN
        if isinstance(screen, RegisterScreen):
            screen.go_login.connect(lambda: self.switch_page(LoginScreen))

        # diğer ekranlar
        if isinstance(screen, JobListingScreen):
            screen.job_selected.connect(lambda j_id: self.switch_page(JobDetailScreen, j_id))
        elif isinstance(screen, JobDetailScreen):
            screen.go_back.connect(lambda: self.switch_page(JobListingScreen))

        self.stack.addWidget(screen)
        self.stack.setCurrentWidget(screen)

    def show_auth(self):
        self.sidebar.hide()
        self.switch_page(LoginScreen)

    def after_login(self):
        self.sidebar.show()
        user = AuthManager.current_user

        # Debug satırı kalsın, kiminle girdiğini gör (İşin bitince silersin)
        print(f"GİRİŞ BAŞARILI | Kullanıcı: {user.username} | Rol: {user.role}")

        self.ui.lbl_username.setText(f"{user.username}\n({user.role})")

        # --- YETKİ KONTROLÜ (Visibility) ---

        # Rolü 'admin' olanlar her şeyi görebilir mi?
        # Yoksa sadece admin panelini mi görsünler? Aşağıdaki mantık en temizi:

        rol = user.role.lower()  # Büyük/küçük harf duyarlılığını bitirelim

        # Admin Paneli Butonu: Sadece admin görsün
        self.ui.btn_admin.setVisible(rol == "admin")

        # İşveren Paneli Butonu: Sadece employer (işveren) veya admin görsün
        self.ui.btn_employer.setVisible(rol == "employer" or rol == "admin")

        # Başvurularım Butonu: Sadece iş arayanlar (jobseeker) görsün
        # Not: Görsellerinde 'jobseeker' veya 'Job Seeker' yazıyor,
        # veritabanında hangisi varsa ona göre kontrol et.
        self.ui.btn_apps.setVisible(rol in ["jobseeker", "job seeker", "seeker"])

        # --- SAYFA YÖNLENDİRMESİ ---
        # Giriş yapınca herkesi önce ilanlara gönderelim
        self.switch_page(JobListingScreen)

    def logout(self):
        AuthManager.logout()
        self.show_auth()