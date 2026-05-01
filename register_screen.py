from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtCore import Signal
from base_widget import BaseWidget
from auth_manager import AuthManager
from ui_register_screen import Ui_Form


class RegisterScreen(BaseWidget):
    register_success = Signal()
    go_login = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)   # 🔥 kritik

        self.setup_connections()

    def setup_connections(self):
        self.ui.registerBtn.clicked.connect(self.do_register)
        self.ui.loginBtn.clicked.connect(self.go_login.emit)

    def do_register(self):
        username = self.ui.username_input.text().strip()
        email = self.ui.email_input.text().strip()
        password = self.ui.password_input.text().strip()
        password2 = self.ui.password2_input.text().strip()
        role = self.ui.role_combo.currentText()

        if password != password2:
            self.show_message("Error", "Passwords do not match.", "error")
            return

        ok, msg = AuthManager.register(username, password, email, role)

        if ok:
            self.show_message("Success", msg, "success")
            self.register_success.emit()
        else:
            self.show_message("Error", msg, "error")
