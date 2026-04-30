from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QComboBox
)
from PySide6.QtCore import Qt, Signal
from base_widget import BaseWidget
from auth_manager import AuthManager


class RegisterScreen(BaseWidget):
    register_success = Signal()
    go_login = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.setMinimumWidth(400)
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(12)
        layout.setContentsMargins(60, 30, 60, 30)

        title = QLabel("Kayıt Ol")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 8px;")
        layout.addWidget(title)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Kullanıcı adı")
        self.username_input.setMinimumHeight(36)
        layout.addWidget(self.username_input)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("E-posta")
        self.email_input.setMinimumHeight(36)
        layout.addWidget(self.email_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Şifre")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMinimumHeight(36)
        layout.addWidget(self.password_input)

        self.password2_input = QLineEdit()
        self.password2_input.setPlaceholderText("Şifre tekrar")
        self.password2_input.setEchoMode(QLineEdit.Password)
        self.password2_input.setMinimumHeight(36)
        layout.addWidget(self.password2_input)

        role_label = QLabel("Hesap türü:")
        layout.addWidget(role_label)

        self.role_combo = QComboBox()
        self.role_combo.addItem("İş Arayan", "jobseeker")
        self.role_combo.addItem("İşveren", "employer")
        self.role_combo.setMinimumHeight(36)
        layout.addWidget(self.role_combo)

        register_btn = QPushButton("Kayıt Ol")
        register_btn.setMinimumHeight(38)
        register_btn.setStyleSheet("background-color: #16a34a; color: white; border-radius: 6px; font-size: 14px;")
        register_btn.clicked.connect(self.do_register)
        layout.addWidget(register_btn)

        back_layout = QHBoxLayout()
        back_layout.addWidget(QLabel("Zaten hesabın var mı?"))
        back_btn = QPushButton("Giriş Yap")
        back_btn.setFlat(True)
        back_btn.setStyleSheet("color: #2563eb; font-weight: bold;")
        back_btn.clicked.connect(self.go_login.emit)
        back_layout.addWidget(back_btn)
        back_layout.addStretch()
        layout.addLayout(back_layout)

    def do_register(self):
        username = self.username_input.text().strip()
        email = self.email_input.text().strip()
        password = self.password_input.text().strip()
        password2 = self.password2_input.text().strip()
        role = self.role_combo.currentData()

        if password != password2:
            self.show_message("Hata", "Şifreler eşleşmiyor.", "error")
            return

        ok, msg = AuthManager.register(username, password, email, role)
        if ok:
            self.show_message("Başarılı", msg, "success")
            self.register_success.emit()
        else:
            self.show_message("Hata", msg, "error")
