from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QComboBox, QFrame
)
from PySide6.QtCore import Qt, Signal
from base_widget import BaseWidget
from auth_manager import AuthManager


class LoginScreen(BaseWidget):
    login_success = Signal()
    go_register = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.setMinimumWidth(400)
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(12)
        layout.setContentsMargins(60, 40, 60, 40)

        title = QLabel("İş Başvuru Sistemi")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 22px; font-weight: bold; margin-bottom: 10px;")
        layout.addWidget(title)

        sub = QLabel("Giriş Yap")
        sub.setAlignment(Qt.AlignCenter)
        sub.setStyleSheet("font-size: 16px; color: gray;")
        layout.addWidget(sub)

        layout.addSpacing(10)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Kullanıcı adı")
        self.username_input.setMinimumHeight(36)
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Şifre")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMinimumHeight(36)
        layout.addWidget(self.password_input)

        login_btn = QPushButton("Giriş Yap")
        login_btn.setMinimumHeight(38)
        login_btn.setStyleSheet("background-color: #2563eb; color: white; border-radius: 6px; font-size: 14px;")
        login_btn.clicked.connect(self.do_login)
        layout.addWidget(login_btn)

        layout.addSpacing(6)

        reg_layout = QHBoxLayout()
        reg_layout.addWidget(QLabel("Hesabın yok mu?"))
        reg_btn = QPushButton("Kayıt ol")
        reg_btn.setFlat(True)
        reg_btn.setStyleSheet("color: #2563eb; font-weight: bold;")
        reg_btn.clicked.connect(self.go_register.emit)
        reg_layout.addWidget(reg_btn)
        reg_layout.addStretch()
        layout.addLayout(reg_layout)

        self.password_input.returnPressed.connect(self.do_login)

    def do_login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        if not username or not password:
            self.show_message("Hata", "Kullanıcı adı ve şifre boş bırakılamaz.", "error")
            return
        ok, msg = AuthManager.login(username, password)
        if ok:
            self.login_success.emit()
        else:
            self.show_message("Giriş Başarısız", msg, "error")
