from PySide6.QtWidgets import QFrame, QLabel, QWidget
from PySide6.QtCore import Qt, Signal
from base_widget import BaseWidget
from job import Job, JobCategory  # JobCategory'yi de import ediyoruz
from ui_job_listing_screen import Ui_Form  # Ana ekran tasarımı
from ui_job_card import Ui_JobCard  # Yeni kart tasarımı


class JobCard(QFrame):
    """Designer ile tasarlanan ilan kartı sınıfı"""
    clicked = Signal(int)

    def __init__(self, job, parent=None):
        super().__init__(parent)
        self.ui = Ui_JobCard()
        self.ui.setupUi(self)  # Tasarımı ve CSS'i yükler
        self.job = job

        # Verileri etiketlere basıyoruz
        self.ui.lbl_title.setText(job.title)
        self.ui.lbl_date.setText(job.created_at[:10] if job.created_at else "")
        self.ui.lbl_company.setText(f"🏢 {job.company}")
        self.ui.lbl_location.setText(f"📍 {job.location}")
        self.ui.lbl_salary.setText(f"💰 {job.salary or 'Belirtilmemiş'}")

    def mousePressEvent(self, event):
        """Karta tıklandığında ilan ID'sini fırlatır"""
        self.clicked.emit(self.job.id)


class JobListingScreen(BaseWidget):
    job_selected = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # Ana ekran tasarımını yükler

        # 1. Kategorileri veritabanından ComboBox'a yükle
        self.load_categories()

        # 2. Buton bağlantıları
        self.ui.btn_search.clicked.connect(self.do_search)
        self.ui.btn_reset.clicked.connect(self.reset_filters)

        # 3. İlanları başlangıçta getir
        self.load_jobs()

    def load_categories(self):
        """Veritabanındaki kategorileri ID'leri ile birlikte kutuya doldurur"""
        self.ui.combo_category.clear()
        # İlk seçenek 'Tümü' (Verisi None olur, SQL'de filtreyi devre dışı bırakır)
        self.ui.combo_category.addItem("Tüm Kategoriler", None)

        # JobCategory sınıfını kullanarak DB'deki tüm kategorileri çek
        categories = JobCategory.get_all()
        for cat in categories:
            # addItem(Görünen İsim, Arka Plandaki Veri/ID)
            self.ui.combo_category.addItem(cat.name, cat.id)

    def load_jobs(self, jobs=None):
        """İlanları listeye dizer"""
        layout = self.ui.jobs_container.layout()

        # Temizlik: Mevcut kartları sil, Spacer'ı (mavi yay) koru
        while layout.count() > 1:
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        jobs = jobs if jobs is not None else Job.get_all()
        self.ui.lbl_count.setText(f"{len(jobs)} ilan bulundu")

        if not jobs:
            lbl = QLabel("Hiç ilan bulunamadı.")
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setStyleSheet("color: gray; margin-top: 40px;")
            layout.insertWidget(0, lbl)
            return

        for job in jobs:
            card = JobCard(job)
            card.clicked.connect(self.job_selected.emit)
            # Kartı Spacer'ın üzerine yerleştir
            layout.insertWidget(layout.count() - 1, card)

    def do_search(self):
        """Seçili kategori ID'sine ve metinlere göre filtreleme yapar"""
        keyword = self.ui.txt_search.text()
        location = self.ui.txt_location.text()

        # Seçili olan kategorinin arka planda tutulan ID değerini alıyoruz
        category_id = self.ui.combo_category.currentData()

        # Veritabanı sorgusunu çalıştır
        results = Job.search(
            keyword=keyword,
            category_id=category_id,
            location=location
        )
        self.load_jobs(results)

    def reset_filters(self):
        """Filtreleri temizler ve listeyi tazeler"""
        self.ui.txt_search.clear()
        self.ui.txt_location.clear()
        self.ui.combo_category.setCurrentIndex(0)
        self.load_jobs()