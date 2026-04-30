from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QStackedWidget, QFrame, QSizePolicy
)
from PySide6.QtCore import Qt
from auth_manager import AuthManager
from notification_manager import NotificationManager

from login_screen import LoginScreen
from register_screen import RegisterScreen
from job_listing_screen import JobListingScreen
from job_detail_screen import JobDetailScreen
from profile_screen import ProfileScreen
from application_screen import ApplicationScreen
from employer_dashboard import EmployerDashboard
from admin_panel import AdminPanel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("İş İlan Sistemi")
        self.setMinimumSize(900, 620)
        self.central = QWidget()
        self.setCentralWidget(self.central)
        self.main_layout = QHBoxLayout(self.central)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.sidebar = QFrame()
        self.sidebar.setFixedWidth(200)
        self.sidebar.setStyleSheet("background-color: #1e293b;")
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_layout.setContentsMargins(0, 0, 0, 0)
        self.sidebar_layout.setSpacing(0)

        self.stack = QStackedWidget()

        self.main_layout.addWidget(self.sidebar)
        self.main_layout.addWidget(self.stack)

        self.show_auth()

    # ── Auth ──────────────────────────────────────
    def show_auth(self):
        self.sidebar.hide()
        self.clear_stack()
        login = LoginScreen()
        login.login_success.connect(self.after_login)
        login.go_register.connect(self.show_register)
        self.stack.addWidget(login)
        self.stack.setCurrentWidget(login)

    def show_register(self):
        self.clear_stack()
        reg = RegisterScreen()
        reg.register_success.connect(self.show_auth)
        reg.go_login.connect(self.show_auth)
        self.stack.addWidget(reg)
        self.stack.setCurrentWidget(reg)

    def after_login(self):
        self.sidebar.show()
        self.build_sidebar()
        self.show_job_listing()

    # ── Sidebar ───────────────────────────────────
    def build_sidebar(self):
        while self.sidebar_layout.count():
            item = self.sidebar_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        user = AuthManager.current_user

        logo = QLabel("🗂 İş İlan Sistemi")
        logo.setStyleSheet("color: white; font-size: 15px; font-weight: bold; padding: 20px 14px 10px 14px;")
        logo.setWordWrap(True)
        self.sidebar_layout.addWidget(logo)

        user_lbl = QLabel(f"{user.username}\n({user.role})")
        user_lbl.setStyleSheet("color: #94a3b8; font-size: 12px; padding: 0 14px 14px 14px;")
        self.sidebar_layout.addWidget(user_lbl)

        sep = QFrame()
        sep.setFrameShape(QFrame.HLine)
        sep.setStyleSheet("color: #334155;")
        self.sidebar_layout.addWidget(sep)

        def make_btn(text, callback):
            btn = QPushButton(text)
            btn.setStyleSheet("""
                QPushButton {
                    color: #cbd5e1; background: transparent; border: none;
                    text-align: left; padding: 12px 18px; font-size: 13px;
                }
                QPushButton:hover { background-color: #334155; color: white; }
            """)
            btn.clicked.connect(callback)
            self.sidebar_layout.addWidget(btn)

        make_btn("🔍  İlanları Gözat", self.show_job_listing)

        if AuthManager.is_jobseeker():
            make_btn("📋  Başvurularım", self.show_applications)

        if AuthManager.is_employer():
            make_btn("🏢  İşveren Paneli", self.show_employer_dashboard)

        if AuthManager.is_admin():
            make_btn("⚙️  Admin Paneli", self.show_admin_panel)

        make_btn("👤  Profilim", self.show_profile)

        notif_count = NotificationManager.unread_count(user.id)
        notif_text = f"🔔  Bildirimler ({notif_count})" if notif_count else "🔔  Bildirimler"
        make_btn(notif_text, self.show_notifications)

        self.sidebar_layout.addStretch()

        logout_btn = QPushButton("🚪  Çıkış Yap")
        logout_btn.setStyleSheet("""
            QPushButton {
                color: #f87171; background: transparent; border: none;
                text-align: left; padding: 12px 18px; font-size: 13px;
            }
            QPushButton:hover { background-color: #450a0a; }
        """)
        logout_btn.clicked.connect(self.logout)
        self.sidebar_layout.addWidget(logout_btn)

    # ── Sayfalar ──────────────────────────────────
    def show_job_listing(self):
        self.clear_stack()
        screen = JobListingScreen()
        screen.job_selected.connect(self.show_job_detail)
        self.stack.addWidget(screen)
        self.stack.setCurrentWidget(screen)

    def show_job_detail(self, job_id):
        self.clear_stack()
        screen = JobDetailScreen(job_id)
        screen.go_back.connect(self.show_job_listing)
        self.stack.addWidget(screen)
        self.stack.setCurrentWidget(screen)

    def show_profile(self):
        self.clear_stack()
        screen = ProfileScreen()
        self.stack.addWidget(screen)
        self.stack.setCurrentWidget(screen)

    def show_applications(self):
        self.clear_stack()
        screen = ApplicationScreen()
        self.stack.addWidget(screen)
        self.stack.setCurrentWidget(screen)

    def show_employer_dashboard(self):
        self.clear_stack()
        screen = EmployerDashboard()
        self.stack.addWidget(screen)
        self.stack.setCurrentWidget(screen)

    def show_admin_panel(self):
        self.clear_stack()
        screen = AdminPanel()
        self.stack.addWidget(screen)
        self.stack.setCurrentWidget(screen)

    def show_notifications(self):
        from notification_screen import NotificationScreen
        self.clear_stack()
        screen = NotificationScreen()
        self.stack.addWidget(screen)
        self.stack.setCurrentWidget(screen)
        self.build_sidebar()  # Sayacı sıfırla

    def logout(self):
        AuthManager.logout()
        self.sidebar.hide()
        self.show_auth()

    def clear_stack(self):
        while self.stack.count():
            w = self.stack.widget(0)
            self.stack.removeWidget(w)
            w.deleteLater()
