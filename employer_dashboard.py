from PySide6.QtWidgets import QDialog, QTableWidgetItem, QPushButton, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from base_widget import BaseWidget
from job import Job, JobCategory
from application import Application, ApplicationStatus
from auth_manager import AuthManager
from notification_manager import NotificationManager

# Designer'dan çevirdiğin dosyaları import ediyoruz
from ui_employer_dashboard import Ui_Form
from ui_add_job_dialog import Ui_AddJobDialog


class AddJobDialog(QDialog):
    """Yeni ilan ekleme ve düzenleme penceresi"""

    def __init__(self, parent=None, job=None):
        super().__init__(parent)
        self.ui = Ui_AddJobDialog()
        self.ui.setupUi(self)
        self.job = job

        # Kategorileri veritabanından çekip ComboBox'ı doldur
        self.populate_categories()

        # Eğer düzenleme modundaysak verileri doldur
        if self.job:
            self.setWindowTitle("İlan Düzenle")
            self.fill_data()

        # Buton bağlantıları
        self.ui.btn_save.clicked.connect(self.accept)
        self.ui.btn_cancel.clicked.connect(self.reject)

    def populate_categories(self):
        self.ui.combo_category.clear()
        for cat in JobCategory.get_all():
            self.ui.combo_category.addItem(cat.name, cat.id)

    def fill_data(self):
        self.ui.txt_title.setText(self.job.title)
        self.ui.txt_company.setText(self.job.company)
        self.ui.txt_location.setText(self.job.location)
        self.ui.txt_salary.setText(self.job.salary or "")
        self.ui.txt_description.setPlainText(self.job.description or "")
        # Kategoriyi seçili getir
        index = self.ui.combo_category.findData(self.job.category_id)
        if index >= 0:
            self.ui.combo_category.setCurrentIndex(index)

    def get_data(self):
        """Penceredeki verileri sözlük olarak döndürür"""
        return {
            "title": self.ui.txt_title.text().strip(),
            "company": self.ui.txt_company.text().strip(),
            "location": self.ui.txt_location.text().strip(),
            "salary": self.ui.txt_salary.text().strip(),
            "category_id": self.ui.combo_category.currentData(),
            "description": self.ui.txt_description.toPlainText().strip()
        }


class EmployerDashboard(BaseWidget):
    """İşveren ana paneli"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.user = AuthManager.current_user

        # Başlığı güncelle
        self.ui.lbl_header.setText(f"İşveren Paneli — {self.user.username}")

        # Designer'daki butonları fonksiyonlara bağla
        self.ui.btn_add_job.clicked.connect(self.add_job)
        self.ui.btn_accept.clicked.connect(lambda: self.change_app_status("accepted"))
        self.ui.btn_reject.clicked.connect(lambda: self.change_app_status("rejected"))

        # Tabloları doldur
        self.refresh_jobs()
        self.refresh_apps()

    def refresh_jobs(self):
        """İlanlarım tablosunu günceller"""
        jobs = Job.get_by_employer(self.user.id)
        self.ui.jobs_table.setRowCount(len(jobs))
        for i, job in enumerate(jobs):
            self.ui.jobs_table.setItem(i, 0, QTableWidgetItem(str(job.id)))
            self.ui.jobs_table.setItem(i, 1, QTableWidgetItem(job.title))
            self.ui.jobs_table.setItem(i, 2, QTableWidgetItem(job.company))
            self.ui.jobs_table.setItem(i, 3, QTableWidgetItem(job.location))

            # Durum sütunu renklendirme
            durum = "Aktif" if job.is_active else "Pasif"
            status_item = QTableWidgetItem(durum)
            status_item.setForeground(QColor("#16a34a") if job.is_active else QColor("#dc2626"))
            self.ui.jobs_table.setItem(i, 4, status_item)

            # Sil butonu hücresi
            del_btn = QPushButton("Sil")
            del_btn.setStyleSheet("color: #dc2626; border: none; font-weight: bold;")
            del_btn.clicked.connect(lambda _, j=job: self.delete_job(j))
            self.ui.jobs_table.setCellWidget(i, 5, del_btn)

    def refresh_apps(self):
        """Başvurular tablosunu günceller"""
        jobs = Job.get_by_employer(self.user.id)
        all_apps = []
        for job in jobs:
            for app in Application.get_by_job(job.id):
                all_apps.append((job, app))

        self.ui.apps_table.setRowCount(len(all_apps))
        status_colors = {"pending": "#fef3c7", "accepted": "#dcfce7", "rejected": "#fee2e2"}

        for i, (job, app) in enumerate(all_apps):
            self.ui.apps_table.setItem(i, 0, QTableWidgetItem(str(app["id"])))
            self.ui.apps_table.setItem(i, 1, QTableWidgetItem(job.title))
            self.ui.apps_table.setItem(i, 2, QTableWidgetItem(app["username"]))
            self.ui.apps_table.setItem(i, 3, QTableWidgetItem(app["email"]))
            self.ui.apps_table.setItem(i, 4, QTableWidgetItem(str(app["applied_at"])[:10]))

            status_label = ApplicationStatus.LABELS.get(app["status"], app["status"])
            status_item = QTableWidgetItem(status_label)
            status_item.setBackground(QColor(status_colors.get(app["status"], "#ffffff")))
            status_item.setTextAlignment(Qt.AlignCenter)
            self.ui.apps_table.setItem(i, 5, status_item)

    def add_job(self):
        dialog = AddJobDialog(self)
        if dialog.exec() == QDialog.Accepted:
            data = dialog.get_data()
            if not data["title"] or not data["company"] or not data["location"]:
                self.show_message("Hata", "Başlık, şirket ve konum zorunludur.", "error")
                return
            Job.create(self.user.id, data["category_id"], data["title"], data["company"],
                       data["location"], data["salary"], data["description"])
            self.show_message("Başarılı", "İlan eklendi.", "success")
            self.refresh_jobs()

    def delete_job(self, job):
        if self.show_confirm("Sil", f'"{job.title}" ilanı silinecek. Emin misiniz?'):
            job.delete()
            self.refresh_jobs()

    def change_app_status(self, new_status):
        row = self.ui.apps_table.currentRow()
        if row < 0:
            self.show_message("Uyarı", "Lütfen bir başvuru seçin.", "warning")
            return
        app_id = int(self.ui.apps_table.item(row, 0).text())
        Application.update_status(app_id, new_status)
        app = Application.get_by_id(app_id)
        if app:
            msg = "Başvurunuz kabul edildi!" if new_status == "accepted" else "Başvurunuz reddedildi."
            NotificationManager.send(app.applicant_id, msg)
        self.refresh_apps()