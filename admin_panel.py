from PySide6.QtWidgets import QTableWidgetItem, QPushButton, QLabel, QHBoxLayout, QWidget, QHeaderView
from PySide6.QtCore import Qt
# 🔥 HATA BURADAYDI: Bu satırın mutlaka en üstte olması lazım!
from base_widget import BaseWidget
from user import User
from job import Job
from report_generator import ReportGenerator

# Designer'dan çevirdiğin dosyayı buraya ekliyoruz
from ui_admin_panel import Ui_Form


class AdminPanel(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Designer tasarımını yükle
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Buton Bağlantıları
        self.ui.btn_delete_user.clicked.connect(self.delete_user)
        self.ui.btn_delete_job.clicked.connect(self.delete_job)
        self.ui.btn_refresh_report.clicked.connect(self.refresh_report)

        # Tabloları ve Raporları doldur
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
        # 2. FOTODAKİ GİZEM BURADA: Rapor alanını önce temizliyoruz
        # Designer'da report_container içine attığın layout'u buluyoruz
        layout = self.ui.report_container.layout()

        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # Özet verileri (Toplam Kullanıcı vb.) çekip dinamik kutucuklar yapıyoruz
        summary = ReportGenerator.get_summary()
        for key, val in summary.items():
            container = QWidget()
            container.setStyleSheet("border: 1px solid #e2e8f0; border-radius: 8px; padding: 10px; background: white;")
            row = QHBoxLayout(container)

            lbl = QLabel(f"<b>{key}:</b>")
            val_lbl = QLabel(str(val))
            val_lbl.setStyleSheet("font-size: 18px; font-weight: bold; color: #2563eb;")

            row.addWidget(lbl)
            row.addWidget(val_lbl)
            row.addStretch()
            layout.addWidget(container)

        # En çok başvuru alanları liste olarak ekliyoruz
        top_label = QLabel("\n<b>En Çok Başvuru Alan İlanlar:</b>")
        layout.addWidget(top_label)

        for r in ReportGenerator.top_jobs():
            lbl = QLabel(f"  • {r['title']} ({r['company']}) → {r['app_count']} başvuru")
            layout.addWidget(lbl)

        layout.addStretch()  # Her şeyi yukarı itmek için alta yay atıyoruz
