from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QTableWidgetItem, QHeaderView, QAbstractItemView

from base_widget import BaseWidget
from application import Application, ApplicationStatus
from auth_manager import AuthManager
from ui_application_screen import Ui_Form


class ApplicationScreen(BaseWidget):
    """İş arayan kullanıcının yapmış olduğu tüm başvuruları listeleyen ekran."""

    def __init__(self, parent=None):
        """
        Uygulama ekranını başlatır, arayüz bileşenlerini yükler,
        tablo ayarlarını yapar ve mevcut başvuruları veritabanından çeker.
        """
        super().__init__(parent)

        # Designer'dan gelen arayüzü kurar
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Tablo görsel ayarlarını yapar ve verileri yükler
        self.setup_table()
        self.load_applications()

    def setup_table(self):
        """
        Başvuru tablosunun görsel ve işlevsel ayarlarını (düzenleme engeli,
        satır seçimi, sütun genişletme vb.) yapılandırır.
        """
        table = self.ui.table

        # Tablo hücrelerinin doğrudan düzenlenmesini engeller
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Sadece satır bazlı seçime izin verir
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Satırların ardışık olarak farklı renklerde görünmesini sağlar
        table.setAlternatingRowColors(True)
        # Satır numaralarının olduğu sütunu gizler
        table.verticalHeader().setVisible(False)

        # İlan başlığı ve Şirket sütunlarını tablo genişliğine göre otomatik yayar
        table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

    def load_applications(self):
        """
        Oturum açmış olan iş arayanın tüm başvurularını veritabanından çeker
        ve durumlarına göre renklendirerek tabloya doldurur.
        """
        table = self.ui.table
        # Mevcut kullanıcının ID'sine göre başvuruları getirir
        apps = Application.get_by_applicant(AuthManager.current_user.id)

        table.setRowCount(len(apps))

        # Başvuru durumlarına göre arka plan renk tanımları
        status_colors = {
            "pending": "#fef3c7",  # Beklemede (Sarımsı)
            "accepted": "#dcfce7", # Kabul Edildi (Yeşilimsi)
            "rejected": "#fee2e2"  # Reddedildi (Kırmızımsı)
        }

        for i, row in enumerate(apps):
            # Hücre verilerini tabloya yerleştirir
            table.setItem(i, 0, QTableWidgetItem(str(row["id"])))
            table.setItem(i, 1, QTableWidgetItem(row["job_title"]))
            table.setItem(i, 2, QTableWidgetItem(row["company"]))
            table.setItem(i, 3, QTableWidgetItem(row["applied_at"][:10]))

            # Başvuru durumunu alıp Türkçe etiketini ve rengini ayarlar
            status = row["status"]
            status_lbl = ApplicationStatus.LABELS.get(status, status)

            status_item = QTableWidgetItem(status_lbl)
            status_item.setBackground(QColor(status_colors.get(status, "#ffffff")))
            status_item.setTextAlignment(Qt.AlignCenter)

            table.setItem(i, 4, status_item)

        # Eğer kullanıcının hiç başvurusu yoksa bilgi mesajı gösterir
        if not apps:
            table.setRowCount(1)
            empty = QTableWidgetItem("Henüz bir başvurunuz bulunmuyor.")
            empty.setTextAlignment(Qt.AlignCenter)
            table.setItem(0, 0, empty)
            # Mesajın tüm sütunlara yayılmasını sağlar
            table.setSpan(0, 0, 1, 5)