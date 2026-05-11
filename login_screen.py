from PySide6.QtCore import Signal
from base_widget import BaseWidget
from auth_manager import AuthManager
# Yeni oluşturduğumuz tasarım dosyasını içeri aktarıyoruz
from ui_login_screen import Ui_Form


class LoginScreen(BaseWidget):
    """Kullanıcıların sisteme giriş yapmasını sağlayan giriş ekranı sınıfı."""

    # Giriş başarılı olduğunda tetiklenecek sinyal
    login_success = Signal()
    # Kayıt ekranına yönlendirme yapıldığında tetiklenecek sinyal
    go_register = Signal()

    def __init__(self, parent=None):
        """
        Giriş ekranını başlatır, Designer ile hazırlanan arayüzü yükler
        ve buton tıklama gibi olayları ilgili fonksiyonlara bağlar.
        """
        super().__init__(parent)

        # Tasarımı başlatıyoruz
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Şifre alanını gizli moda geçirir (karakterler nokta olarak görünür)
        from PySide6.QtWidgets import QLineEdit
        self.ui.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        # Buton bağlantıları (Designer'da tanımlanan isimlerle bağlanıyor)
        self.ui.login_btn.clicked.connect(self.do_login)
        self.ui.reg_btn.clicked.connect(self.go_register.emit)

        # Şifre alanında Enter tuşuna basıldığında giriş yapma fonksiyonunu tetikler
        self.ui.password_input.returnPressed.connect(self.do_login)

    def do_login(self):
        """
        Arayüzdeki giriş alanlarından verileri çeker, boş alan kontrolü yapar
        ve AuthManager üzerinden kullanıcı kimlik doğrulamasını gerçekleştirir.
        """
        # Kullanıcı adı ve şifre verilerini yanlardaki boşlukları temizleyerek alıyoruz
        username = self.ui.username_input.text().strip()
        password = self.ui.password_input.text().strip()

        # Zorunlu alan kontrolü
        if not username or not password:
            self.show_message("Hata", "Kullanıcı adı ve şifre boş bırakılamaz.", "error")
            return

        # Kimlik doğrulama işlemini başlatıyoruz
        ok, msg = AuthManager.login(username, password)
        if ok:
            # Giriş başarılıysa başarı sinyalini yayar
            self.login_success.emit()
        else:
            # Giriş başarısızsa kullanıcıya hata mesajı gösterir
            self.show_message("Giriş Başarısız", msg, "error")