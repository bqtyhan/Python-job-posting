from PySide6.QtWidgets import QTableWidgetItem, QHeaderView, QLabel, QHBoxLayout, QWidget
from PySide6.QtCore import Qt
from base_widget import BaseWidget
from user import User
from job import Job
from report_generator import ReportGenerator

# Designer'dan çevirdiğin tasarım dosyası
from ui_admin_panel import Ui_Form


class AdminPanel(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # --- BUTON BAĞLANTILARI ---
        self.ui.btn_delete_user.clicked.connect(self.delete_user)
        self.ui.btn_delete_job.clicked.connect(self.delete_job)
        self.ui.btn_refresh_report.clicked.connect(self.refresh_report)

        # Tablo sütunlarını otomatik genişlet
        self.ui.users_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.jobs_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Verileri ilk açılışta yükle
        self.refresh_users()
        self.refresh_jobs()
        self.refresh_report()

    def refresh_users(self):
        users = User.get_all()
        self.ui.users_table.setRowCount(len(users))
        for i, u in enumerate(users):
            self.ui.users_table.setItem(i, 0, QTableWidgetItem(str(u.id)))
            self.ui.users_table.setItem(i, 1, QTableWidgetItem(u.username))
            self.ui.users_table.setItem(i, 2, QTableWidgetItem(u.email))
            self.ui.users_table.setItem(i, 3, QTableWidgetItem(u.role))
            self.ui.users_table.setItem(i, 4, QTableWidgetItem(str(u.created_at)[:10] if u.created_at else ""))

    def refresh_jobs(self):
        jobs = Job.get_all(active_only=False)
        self.ui.jobs_table.setRowCount(len(jobs))
        for i, job in enumerate(jobs):
            self.ui.jobs_table.setItem(i, 0, QTableWidgetItem(str(job.id)))
            self.ui.jobs_table.setItem(i, 1, QTableWidgetItem(job.title))
            self.ui.jobs_table.setItem(i, 2, QTableWidgetItem(job.company))
            self.ui.jobs_table.setItem(i, 3, QTableWidgetItem(job.location))
            self.ui.jobs_table.setItem(i, 4, QTableWidgetItem("Aktif" if job.is_active else "Pasif"))
            self.ui.jobs_table.setItem(i, 5, QTableWidgetItem(str(job.created_at)[:10] if job.created_at else ""))

    def refresh_report(self):
        # Designer'daki report_container içindeki layout'u bul
        layout = self.ui.report_container.layout()
        if not layout: return

        # Eski rapor kutularını temizle
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # Yeni rapor verilerini bas
        summary = ReportGenerator.get_summary()
        for key, val in summary.items():
            container = QWidget()
            container.setStyleSheet("border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px; background: white;")
            row = QHBoxLayout(container)
            row.addWidget(QLabel(f"<b>{key}:</b>"))
            val_lbl = QLabel(str(val))
            val_lbl.setStyleSheet("font-size: 18px; font-weight: bold; color: #2563eb;")
            row.addWidget(val_lbl)
            row.addStretch()
            layout.addWidget(container)

        top_label = QLabel("\n<b>En Çok Başvuru Alan İlanlar:</b>")
        layout.addWidget(top_label)
        for r in ReportGenerator.top_jobs():
            lbl = QLabel(f"  • {r['title']} ({r['company']}) → {r['app_count']} başvuru")
            layout.addWidget(lbl)
        layout.addStretch()

    def delete_user(self):
        row = self.ui.users_table.currentRow()
        if row < 0:
            self.show_message("Uyarı", "Lütfen bir kullanıcı seçin.", "warning")
            return

        user_id = int(self.ui.users_table.item(row, 0).text())
        username = self.ui.users_table.item(row, 1).text()

        if self.show_confirm("Sil", f"'{username}' kullanıcısı silinecek. Emin misiniz?"):
            User.delete(user_id)
            self.refresh_users()

    def delete_job(self):
        row = self.ui.jobs_table.currentRow()
        if row < 0:
            self.show_message("Uyarı", "Lütfen bir ilan seçin.", "warning")
            return

        job_id = int(self.ui.jobs_table.item(row, 0).text())
        title = self.ui.jobs_table.item(row, 1).text()

        if self.show_confirm("Sil", f"'{title}' ilanı silinecek. Emin misiniz?"):
            job = Job.get_by_id(job_id)
            if job:
                job.delete()
            self.refresh_jobs()