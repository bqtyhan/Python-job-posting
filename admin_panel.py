from PySide6.QtWidgets import QTableWidgetItem, QHeaderView, QLabel, QHBoxLayout, QWidget
from PySide6.QtCore import Qt
from base_widget import BaseWidget
from user import User
from job import Job
from report_generator import ReportGenerator

# Designer'dan çevrilen tasarım dosyası
from ui_admin_panel import Ui_Form


class AdminPanel(BaseWidget):
    """Sistem yöneticisinin kullanıcıları, ilanları ve istatistiksel raporları yönettiği panel."""

    def __init__(self, parent=None):
        """
        Admin panelini başlatır, kullanıcı arayüzünü yükler, buton bağlantılarını kurar
         ve tabloların otomatik genişleme ayarlarını yaparak ilk verileri yükler.
        """
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # --- BUTON BAĞLANTILARI ---
        self.ui.btn_delete_user.clicked.connect(self.delete_user)
        self.ui.btn_delete_job.clicked.connect(self.delete_job)
        self.ui.btn_refresh_report.clicked.connect(self.refresh_report)

        # Tablo sütunlarını pencere genişliğine göre otomatik genişletir
        self.ui.users_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.jobs_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Panel açıldığında tabloları ve raporu veritabanından güncel verilerle doldurur
        self.refresh_users()
        self.refresh_jobs()
        self.refresh_report()

    def refresh_users(self):
        """Sistemde kayıtlı olan tüm kullanıcıları veritabanından çeker ve kullanıcı tablosuna listeler."""
        users = User.get_all()
        self.ui.users_table.setRowCount(len(users))
        for i, u in enumerate(users):
            self.ui.users_table.setItem(i, 0, QTableWidgetItem(str(u.id)))
            self.ui.users_table.setItem(i, 1, QTableWidgetItem(u.username))
            self.ui.users_table.setItem(i, 2, QTableWidgetItem(u.email))
            self.ui.users_table.setItem(i, 3, QTableWidgetItem(u.role))
            self.ui.users_table.setItem(i, 4, QTableWidgetItem(str(u.created_at)[:10] if u.created_at else ""))

    def refresh_jobs(self):
        """Sistemdeki tüm iş ilanlarını (aktif ve pasif) veritabanından çeker ve ilan tablosuna aktarır."""
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
        """
        Sistem istatistiklerini (toplam kullanıcı, ilan vb.) rapor üreticiden alır,
        arayüzdeki eski rapor öğelerini temizler ve güncel verileri görsel kartlar olarak ekler.
        """
        # Designer'daki report_container içindeki düzenleyiciyi (layout) kontrol eder
        layout = self.ui.report_container.layout()
        if not layout: return

        # Mevcut rapor kutularını bellekten ve arayüzden temizler
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # Özet istatistik verilerini döngü ile arayüze basar
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

        # En çok ilgi gören (başvuru alan) ilanları listeler
        top_label = QLabel("\n<b>En Çok Başvuru Alan İlanlar:</b>")
        layout.addWidget(top_label)
        for r in ReportGenerator.top_jobs():
            lbl = QLabel(f"  • {r['title']} ({r['company']}) → {r['app_count']} başvuru")
            layout.addWidget(lbl)
        layout.addStretch()

    def delete_user(self):
        """Kullanıcı tablosunda seçili olan satırı tespit eder ve onay aldıktan sonra kullanıcıyı sistemden siler."""
        row = self.ui.users_table.currentRow()
        if row < 0:
            self.show_message("Uyarı", "Lütfen bir kullanıcı seçin.", "warning")
            return

        user_id = int(self.ui.users_table.item(row, 0).text())
        username = self.ui.users_table.item(row, 1).text()

        # Silme onayı alır ve veritabanı işlemini tetikler
        if self.show_confirm("Sil", f"'{username}' kullanıcısı silinecek. Emin misiniz?"):
            User.delete(user_id)
            self.refresh_users()

    def delete_job(self):
        """İlan tablosunda seçili olan ilanı tespit eder ve onay aldıktan sonra ilanı sistemden kaldırır."""
        row = self.ui.jobs_table.currentRow()
        if row < 0:
            self.show_message("Uyarı", "Lütfen bir ilan seçin.", "warning")
            return

        job_id = int(self.ui.jobs_table.item(row, 0).text())
        title = self.ui.jobs_table.item(row, 1).text()

        # Silme onayı alır ve ilan nesnesi üzerinden silme işlemini gerçekleştirir
        if self.show_confirm("Sil", f"'{title}' ilanı silinecek. Emin misiniz?"):
            job = Job.get_by_id(job_id)
            if job:
                job.delete()
            self.refresh_jobs()