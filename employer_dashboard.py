from PySide6.QtWidgets import QDialog, QTableWidgetItem, QPushButton, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from base_widget import BaseWidget
from job import Job, JobCategory
from application import Application, ApplicationStatus
from auth_manager import AuthManager

# Designer'dan çevrilen arayüz dosyaları
from ui_employer_dashboard import Ui_Form
from ui_add_job_dialog import Ui_AddJobDialog


class AddJobDialog(QDialog):
    """Yeni ilan ekleme ve mevcut ilanları düzenleme işlemleri için kullanılan diyalog penceresi."""

    def __init__(self, parent=None, job=None):
        """
        Pencere bileşenlerini başlatır, kategorileri yükler ve eğer düzenleme
        modundaysak mevcut ilan bilgilerini alanlara doldurur.
        """
        super().__init__(parent)
        self.ui = Ui_AddJobDialog()
        self.ui.setupUi(self)
        self.job = job

        # Kategorileri veritabanından çekip ComboBox'ı (açılır menü) doldurur
        self.populate_categories()

        # Eğer bir iş nesnesi gönderildiyse düzenleme moduna geçer
        if self.job:
            self.setWindowTitle("İlan Düzenle")
            self.fill_data()

        # Buton tıklama olaylarını bağlar
        self.ui.btn_save.clicked.connect(self.accept)
        self.ui.btn_cancel.clicked.connect(self.reject)

    def populate_categories(self):
        """Veritabanındaki tüm iş kategorilerini alır ve seçim menüsüne ekler."""
        self.ui.combo_category.clear()
        for cat in JobCategory.get_all():
            self.ui.combo_category.addItem(cat.name, cat.id)

    def fill_data(self):
        """Düzenleme modunda, seçilen ilanın mevcut bilgilerini form alanlarına yazar."""
        self.ui.txt_title.setText(self.job.title)
        self.ui.txt_company.setText(self.job.company)
        self.ui.txt_location.setText(self.job.location)
        self.ui.txt_salary.setText(self.job.salary or "")
        self.ui.txt_description.setPlainText(self.job.description or "")

        # Mevcut kategoriyi menüde seçili hale getirir
        index = self.ui.combo_category.findData(self.job.category_id)
        if index >= 0:
            self.ui.combo_category.setCurrentIndex(index)

    def get_data(self):
        """Kullanıcının form alanlarına girdiği verileri bir sözlük yapısında toplar."""
        return {
            "title": self.ui.txt_title.text().strip(),
            "company": self.ui.txt_company.text().strip(),
            "location": self.ui.txt_location.text().strip(),
            "salary": self.ui.txt_salary.text().strip(),
            "category_id": self.ui.combo_category.currentData(),
            "description": self.ui.txt_description.toPlainText().strip()
        }


class EmployerDashboard(BaseWidget):
    """İşverenin ilanlarını yönetebildiği ve başvuruları görüntüleyebildiği ana panel."""

    def __init__(self, parent=None):
        """Panel arayüzünü hazırlar, kullanıcı bilgilerini ayarlar ve tabloları doldurur."""
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.user = AuthManager.current_user

        # Panel başlığına kullanıcı adını ekler
        self.ui.lbl_header.setText(f"İşveren Paneli — {self.user.username}")

        # Arayüzdeki butonları ilgili fonksiyonlara bağlar
        self.ui.btn_add_job.clicked.connect(self.add_job)
        self.ui.btn_accept.clicked.connect(lambda: self.change_app_status("accepted"))
        self.ui.btn_reject.clicked.connect(lambda: self.change_app_status("rejected"))

        # Mevcut verileri tablolara yükler
        self.refresh_jobs()
        self.refresh_apps()

    def refresh_jobs(self):
        """İşverenin yayınladığı ilanları veritabanından çeker ve tabloyu günceller."""
        jobs = Job.get_by_employer(self.user.id)
        self.ui.jobs_table.setRowCount(len(jobs))
        for i, job in enumerate(jobs):
            self.ui.jobs_table.setItem(i, 0, QTableWidgetItem(str(job.id)))
            self.ui.jobs_table.setItem(i, 1, QTableWidgetItem(job.title))
            self.ui.jobs_table.setItem(i, 2, QTableWidgetItem(job.company))
            self.ui.jobs_table.setItem(i, 3, QTableWidgetItem(job.location))

            # İlan durumunu (Aktif/Pasif) belirler ve renklendirir
            durum = "Aktif" if job.is_active else "Pasif"
            status_item = QTableWidgetItem(durum)
            status_item.setForeground(QColor("#16a34a") if job.is_active else QColor("#dc2626"))
            self.ui.jobs_table.setItem(i, 4, status_item)

            # Her satıra özel 'Sil' butonu ekler
            del_btn = QPushButton("Sil")
            del_btn.setStyleSheet("color: #dc2626; border: none; font-weight: bold;")
            del_btn.clicked.connect(lambda _, j=job: self.delete_job(j))
            self.ui.jobs_table.setCellWidget(i, 5, del_btn)

    def refresh_apps(self):
        """İşverenin ilanlarına gelen tüm başvuruları listeler ve durumlarına göre renklendirir."""
        jobs = Job.get_by_employer(self.user.id)
        all_apps = []
        for job in jobs:
            for app in Application.get_by_job(job.id):
                all_apps.append((job, app))

        # Ön yazı sütununu ekle (7 sütun)
        self.ui.apps_table.setColumnCount(7)
        self.ui.apps_table.setHorizontalHeaderLabels(
            ["ID", "İlan", "Başvuran", "E-posta", "Tarih", "Ön Yazı", "Durum"]
        )
        self.ui.apps_table.setRowCount(len(all_apps))
        # Durum kodlarına göre arka plan renkleri
        status_colors = {"pending": "#fef3c7", "accepted": "#dcfce7", "rejected": "#fee2e2"}

        for i, (job, app) in enumerate(all_apps):
            self.ui.apps_table.setItem(i, 0, QTableWidgetItem(str(app["id"])))
            self.ui.apps_table.setItem(i, 1, QTableWidgetItem(job.title))
            self.ui.apps_table.setItem(i, 2, QTableWidgetItem(app["username"]))
            self.ui.apps_table.setItem(i, 3, QTableWidgetItem(app["email"]))
            self.ui.apps_table.setItem(i, 4, QTableWidgetItem(str(app["applied_at"])[:10]))

            # Ön yazıyı gösterir (boşsa tire koyar)
            cover = app["cover_letter"] or "-"
            self.ui.apps_table.setItem(i, 5, QTableWidgetItem(cover))

            # Başvuru durum metnini (Beklemede, Kabul vb.) ayarlar
            status_label = ApplicationStatus.LABELS.get(app["status"], app["status"])
            status_item = QTableWidgetItem(status_label)
            status_item.setBackground(QColor(status_colors.get(app["status"], "#ffffff")))
            status_item.setTextAlignment(Qt.AlignCenter)
            self.ui.apps_table.setItem(i, 6, status_item)

    def add_job(self):
        """Yeni ilan ekleme penceresini açar ve girilen verileri veritabanına kaydeder."""
        dialog = AddJobDialog(self)
        if dialog.exec() == QDialog.Accepted:
            data = dialog.get_data()
            # Zorunlu alan kontrolü
            if not data["title"] or not data["company"] or not data["location"]:
                self.show_message("Hata", "Başlık, şirket ve konum zorunludur.", "error")
                return

            # Yeni ilanı oluşturur
            Job.create(self.user.id, data["category_id"], data["title"], data["company"],
                       data["location"], data["salary"], data["description"])
            self.show_message("Başarılı", "İlan eklendi.", "success")
            self.refresh_jobs()

    def delete_job(self, job):
        """Seçilen ilanı silmeden önce kullanıcıdan onay alır ve veritabanından kaldırır."""
        if self.show_confirm("Sil", f'"{job.title}" ilanı silinecek. Emin misiniz?'):
            job.delete()
            self.refresh_jobs()

    def change_app_status(self, new_status):
        """Seçili başvurunun durumunu (Kabul/Red) günceller."""
        row = self.ui.apps_table.currentRow()
        if row < 0:
            self.show_message("Uyarı", "Lütfen bir başvuru seçin.", "warning")
            return

        # Tablodan başvuru ID'sini alır
        app_id = int(self.ui.apps_table.item(row, 0).text())

        # Mevcut başvuruyu veritabanından çekip durumunu kontrol eder
        app = Application.get_by_id(app_id)
        if app and app.status == ApplicationStatus.REJECTED:
            self.show_message(
                "Uyarı",
                "Reddedilen bir başvurunun durumu değiştirilemez.",
                "warning"
            )
            return

        Application.update_status(app_id, new_status)

        # Görünümü tazelemek için tabloyu yeniden doldurur
        self.refresh_apps()