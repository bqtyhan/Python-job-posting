from PySide6.QtCore import Signal
from base_widget import BaseWidget
from ui_job_detail import Ui_Form
from job import Job
from application import Application
from auth_manager import AuthManager


class JobDetailScreen(BaseWidget):
    """Belirli bir iş ilanının detaylarını gösteren ve başvuru yapılmasını sağlayan ekran."""

    # Geri dön butonuna tıklandığında tetiklenecek sinyal
    go_back = Signal()

    def __init__(self, job_id, parent=None):
        """
        Ekranı başlatır, ilgili iş ilanının verilerini çeker ve arayüz bağlantılarını kurar.

        Args:
            job_id (int): Detayları görüntülenecek iş ilanının kimlik numarası.
        """
        super().__init__(parent)

        # Kullanıcı arayüzünü (UI) yükler
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.job_id = job_id
        self.job = Job.get_by_id(job_id)

        # Verileri doldurur ve buton bağlantılarını ayarlar
        self.setup_data()
        self.setup_connections()

    def setup_data(self):
        """İş ilanına ait başlık, şirket, konum, maaş ve açıklama gibi bilgileri ekrandaki alanlara yerleştirir."""
        if not self.job:
            self.ui.title_lbl.setText("İlan bulunamadı")
            return

        # Temel ilan bilgilerini etiketlere yazar
        self.ui.title_lbl.setText(self.job.title or "-")

        # Başvuru yazısı alanını temizler ve ipucu metni ekler
        self.ui.cover_letter.clear()
        self.ui.cover_letter.setPlaceholderText(
            "Ön yazınızı buraya yazın..."
        )

        self.ui.company_lbl.setText(f"🏢 {self.job.company or '-'}")
        self.ui.location_lbl.setText(f"📍 {self.job.location or '-'}")

        salary = self.job.salary or "Belirtilmemiş"
        self.ui.salary_lbl.setText(f"💰 {salary}")

        # Tarih formatını ayarlar (ilk 10 karakter: YYYY-AA-GG)
        date = (self.job.created_at or "")[:10]
        self.ui.date_lbl.setText(f"📅 {date}" if date else "")

        # İlan açıklamasını ayarlar ve metin kaydırmayı açar
        self.ui.desc_lbl.setText(self.job.description or "Açıklama mevcut değil")
        self.ui.desc_lbl.setWordWrap(True)

    def setup_connections(self):
        """Ekrandaki butonların (Geri, Başvur) tıklama olaylarını ilgili fonksiyonlara bağlar."""
        self.ui.back_btn.clicked.connect(self.go_back.emit)
        self.ui.apply_btn.clicked.connect(self.do_apply)

    def do_apply(self):
        """Kullanıcının yazdığı ön yazı ile birlikte iş ilanına başvuru işlemini gerçekleştirir."""
        # Giriş kontrolü yapar
        if not AuthManager.is_logged_in():
            self.show_message("Uyarı", "Başvurmak için giriş yapmalısınız.", "warning")
            return

        # İşverenin kendi ilanına başvurmasını engeller
        if self.job and AuthManager.current_user.id == self.job.employer_id:
            self.show_message("Uyarı", "Kendi ilanınıza başvuramazsınız.", "warning")
            return

        # Ön yazıyı alır ve boşlukları temizler
        cover = self.ui.cover_letter.toPlainText().strip()

        # Başvuruyu veritabanına kaydeder
        ok, msg = Application.apply(
            self.job_id,
            AuthManager.current_user.id,
            cover
        )

        if ok:
            # Bildirim gönderme (NotificationManager) kısmı kaldırıldı
            self.show_message("Başarılı", msg, "success")
        else:
            self.show_message("Hata", msg, "error")
