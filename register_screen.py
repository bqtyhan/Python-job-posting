from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtCore import Signal
from base_widget import BaseWidget
from auth_manager import AuthManager
from ui_register_screen import Ui_Form


class RegisterScreen(BaseWidget):
    """Yeni kullanıcıların sisteme kayıt olmasını sağlayan ekran sınıfı."""

    # Kayıt işlemi başarıyla tamamlandığında tetiklenecek sinyal
    register_success = Signal()
    # Giriş ekranına geri dönmek için tetiklenecek sinyal
    go_login = Signal()

    def __init__(self, parent=None):
        """
        Kayıt ekranını başlatır, Designer ile hazırlanan arayüzü (UI) yükler
        ve buton bağlantılarını kurar.
        """
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Butonların tıklama olaylarını fonksiyonlara bağlar
        self.setup_connections()

    def setup_connections(self):
        """Arayüzdeki 'Kayıt Ol' ve 'Giriş Yap' butonlarını ilgili fonksiyonlara veya sinyallere bağlar."""
        self.ui.registerBtn.clicked.connect(self.do_register)
        self.ui.loginBtn.clicked.connect(self.go_login.emit)

    def do_register(self):
        """
        Kullanıcının girdiği form verilerini alır, şifrelerin birbiriyle uyumunu kontrol eder
        ve AuthManager üzerinden veritabanına yeni kullanıcı kaydını gerçekleştirir.
        """
        # Form alanlarındaki verileri yan boşluklarını temizleyerek çeker
        username = self.ui.username_input.text().strip()
        email = self.ui.email_input.text().strip()
        password = self.ui.password_input.text().strip()
        password2 = self.ui.password2_input.text().strip()
        role = self.ui.role_combo.currentText()

        # İki şifre alanının birbiriyle aynı olup olmadığını kontrol eder
        if password != password2:
            self.show_message("Hata", "Şifreler birbiriyle eşleşmiyor.", "error")
            return

        # AuthManager üzerinden kayıt işlemini başlatır
        ok, msg = AuthManager.register(username, password, email, role)

        if ok:
            # Kayıt başarılıysa kullanıcıya bilgi verir ve başarı sinyalini yayar
            self.show_message("Başarılı", msg, "success")
            self.register_success.emit()
        else:
            # Bir hata oluştuysa hata mesajını ekranda gösterir
            self.show_message("Hata", msg, "error")