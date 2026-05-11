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
    """Uygulamanın ana penceresi; menüleri, sayfa geçişlerini ve oturum yönetimini koordine eder."""

    def __init__(self):
        """
        Ana pencereyi başlatır, kullanıcı arayüzünü (UI) kurar,
        menü butonlarını ilgili sayfa geçiş fonksiyonlarına bağlar ve başlangıçta giriş ekranını gösterir.
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("İş İlan Sistemi")

        # Arayüz nesnelerini (Yan menü ve sayfa yığını) değişkenlere atar
        self.sidebar = self.ui.left_menu_frame
        self.stack = self.ui.main_pages

        # Sol menüdeki butonların tıklama olaylarını sayfa değiştirme fonksiyonuna bağlar
        self.ui.btn_jobs.clicked.connect(lambda: self.switch_page(JobListingScreen))
        self.ui.btn_apps.clicked.connect(lambda: self.switch_page(ApplicationScreen))
        self.ui.btn_employer.clicked.connect(lambda: self.switch_page(EmployerDashboard))
        self.ui.btn_admin.clicked.connect(lambda: self.switch_page(AdminPanel))
        self.ui.btn_logout.clicked.connect(self.logout)

        # Uygulama açıldığında kimlik doğrulama (Giriş) ekranını gösterir
        self.show_auth()

    def switch_page(self, screen_class, *args):
        """
        QStackedWidget (sayfa yığını) üzerindeki mevcut sayfayı temizler ve yeni sayfayı yükler.
        Sayfalar arasındaki sinyal bağlantılarını (Giriş başarısı, Kayıt ol yönlendirmesi vb.) kurar.

        Args:
            screen_class: Yüklenecek olan sınıfın adı (Örn: LoginScreen).
            *args: Sınıf başlatılırken gönderilecek ek argümanlar.
        """
        # Mevcut sayfaları yığından temizler
        while self.stack.count():
            self.stack.removeWidget(self.stack.widget(0))

        # Yeni ekran nesnesini oluşturur
        screen = screen_class(*args)

        # Giriş ekranı sinyalleri: Kayıt olmaya yönlendirir veya başarılı girişi işler
        if isinstance(screen, LoginScreen):
            screen.go_register.connect(lambda: self.switch_page(RegisterScreen))
            screen.login_success.connect(self.after_login)

        # Kayıt ekranı sinyali: Giriş ekranına geri döndürür
        if isinstance(screen, RegisterScreen):
            screen.go_login.connect(lambda: self.switch_page(LoginScreen))

        # İlan listesi ve detay ekranı arası geçiş sinyalleri
        if isinstance(screen, JobListingScreen):
            screen.job_selected.connect(lambda j_id: self.switch_page(JobDetailScreen, j_id))
        elif isinstance(screen, JobDetailScreen):
            screen.go_back.connect(lambda: self.switch_page(JobListingScreen))

        # Yeni ekranı yığına ekler ve görünür yapar
        self.stack.addWidget(screen)
        self.stack.setCurrentWidget(screen)

    def show_auth(self):
        """Kullanıcı giriş yapmamışken yan menüyü gizler ve ekranda sadece Giriş sayfasını gösterir."""
        self.sidebar.hide()
        self.switch_page(LoginScreen)

    def after_login(self):
        """
        Başarılı giriş sonrasında yan menüyü gösterir, kullanıcı bilgilerini arayüze yazar
        ve kullanıcının rolüne göre (admin, işveren, aday) menü butonlarını kısıtlar.
        """
        self.sidebar.show()
        user = AuthManager.current_user

        # Arayüzdeki kullanıcı adı ve rol bilgisini günceller
        self.ui.lbl_username.setText(f"{user.username}\n({user.role})")

        # Yetki Kontrolü: Kullanıcının rolüne göre menü butonlarını görünür/gizli yapar
        rol = user.role.lower()

        # Admin Paneli: Sadece adminler görebilir
        self.ui.btn_admin.setVisible(rol == "admin")

        # İşveren Paneli: İşverenler ve adminler görebilir
        self.ui.btn_employer.setVisible(rol == "employer" or rol == "admin")

        # Başvurularım: Sadece iş arayanlar (jobseeker) görebilir
        self.ui.btn_apps.setVisible(rol in ["jobseeker", "job seeker", "seeker"])

        # Giriş sonrası herkesi varsayılan olarak ilan listesi sayfasına yönlendirir
        self.switch_page(JobListingScreen)

    def logout(self):
        """Aktif oturumu kapatır ve kullanıcıyı tekrar kimlik doğrulama (Giriş) ekranına döndürür."""
        AuthManager.logout()
        self.show_auth()