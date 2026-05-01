from PySide6.QtCore import Signal
from base_widget import BaseWidget
from auth_manager import AuthManager
# Yeni oluşturduğumuz tasarım dosyasını içeri aktarıyoruz
from ui_login_screen import Ui_Form


class LoginScreen(BaseWidget):
    login_success = Signal()
    go_register = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        # Tasarımı başlatıyoruz
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Buton bağlantıları (Designer'da verdiğin isimlerle)
        self.ui.login_btn.clicked.connect(self.do_login)
        self.ui.reg_btn.clicked.connect(self.go_register.emit)

        # Enter'a basınca giriş yapma
        self.ui.password_input.returnPressed.connect(self.do_login)

    def do_login(self):
        # Verileri çekiyoruz
        username = self.ui.username_input.text().strip()
        password = self.ui.password_input.text().strip()

        if not username or not password:
            self.show_message("Hata", "Kullanıcı adı ve şifre boş bırakılamaz.", "error")
            return

        ok, msg = AuthManager.login(username, password)
        if ok:
            self.login_success.emit()
        else:
            self.show_message("Giriş Başarısız", msg, "error")