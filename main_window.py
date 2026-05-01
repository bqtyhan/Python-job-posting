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
        """Tüm sayfa geçişlerini tek elden yöneten sihirli fonksiyon"""
        while self.stack.count():
            self.stack.removeWidget(self.stack.widget(0))

        screen = screen_class(*args)
        # Özel durum: İlan listesinden detaya geçiş
        if isinstance(screen, JobListingScreen):
            screen.job_selected.connect(lambda j_id: self.switch_page(JobDetailScreen, j_id))
        elif isinstance(screen, JobDetailScreen):
            screen.go_back.connect(lambda: self.switch_page(JobListingScreen))

        self.stack.addWidget(screen)
        self.stack.setCurrentWidget(screen)

    def show_auth(self):
        """Giriş/Kayıt ekranlarını yönetir"""
        self.sidebar.hide()
        login = LoginScreen()
        login.login_success.connect(self.after_login)
        login.go_register.connect(lambda: self.switch_page(RegisterScreen))  # Register'da başarıyı login'e bağla
        self.stack.addWidget(login)
        self.stack.setCurrentWidget(login)

    def after_login(self):
        """Giriş sonrası menüyü hazırlar"""
        self.sidebar.show()
        user = AuthManager.current_user
        self.ui.lbl_username.setText(f"{user.username}\n({user.role})")

        # Yetki Kontrolü (Sadece yetkisi olan butonları göster)
        self.ui.btn_apps.setVisible(AuthManager.is_jobseeker())
        self.ui.btn_employer.setVisible(AuthManager.is_employer())
        self.ui.btn_admin.setVisible(AuthManager.is_admin())

        self.switch_page(JobListingScreen)

    def logout(self):
        AuthManager.logout()
        self.show_auth()
