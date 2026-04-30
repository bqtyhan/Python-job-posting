from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QTableWidget, QTableWidgetItem, QHeaderView,
    QTabWidget, QWidget, QFrame
)
from PySide6.QtCore import Qt
from base_widget import BaseWidget
from user import User
from job import Job
from report_generator import ReportGenerator
from database import db


class AdminPanel(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)

        header = QLabel("Admin Paneli")
        header.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(header)

        tabs = QTabWidget()

        self.users_tab = QWidget()
        self.setup_users_tab()
        tabs.addTab(self.users_tab, "Kullanıcılar")

        self.jobs_tab = QWidget()
        self.setup_jobs_tab()
        tabs.addTab(self.jobs_tab, "Tüm İlanlar")

        self.report_tab = QWidget()
        self.setup_report_tab()
        tabs.addTab(self.report_tab, "Raporlar")

        layout.addWidget(tabs)

    def setup_users_tab(self):
        layout = QVBoxLayout(self.users_tab)
        self.users_table = QTableWidget()
        self.users_table.setColumnCount(5)
        self.users_table.setHorizontalHeaderLabels(["ID", "Kullanıcı Adı", "E-posta", "Rol", "Kayıt Tarihi"])
        self.users_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.users_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.users_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.users_table.setAlternatingRowColors(True)
        self.users_table.verticalHeader().setVisible(False)
        self.users_table.setFrameShape(QFrame.NoFrame)
        layout.addWidget(self.users_table)

        del_btn = QPushButton("Seçili Kullanıcıyı Sil")
        del_btn.setStyleSheet("background-color: #dc2626; color: white; border-radius: 5px; padding: 5px 12px;")
        del_btn.clicked.connect(self.delete_user)
        layout.addWidget(del_btn, alignment=Qt.AlignLeft)
        self.refresh_users()

    def setup_jobs_tab(self):
        layout = QVBoxLayout(self.jobs_tab)
        self.jobs_table = QTableWidget()
        self.jobs_table.setColumnCount(6)
        self.jobs_table.setHorizontalHeaderLabels(["ID", "Başlık", "Şirket", "Konum", "Durum", "Tarih"])
        self.jobs_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.jobs_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.jobs_table.setAlternatingRowColors(True)
        self.jobs_table.verticalHeader().setVisible(False)
        self.jobs_table.setFrameShape(QFrame.NoFrame)
        layout.addWidget(self.jobs_table)

        del_btn = QPushButton("Seçili İlanı Sil")
        del_btn.setStyleSheet("background-color: #dc2626; color: white; border-radius: 5px; padding: 5px 12px;")
        del_btn.clicked.connect(self.delete_job)
        layout.addWidget(del_btn, alignment=Qt.AlignLeft)
        self.refresh_jobs()

    def setup_report_tab(self):
        layout = QVBoxLayout(self.report_tab)
        layout.setSpacing(10)

        refresh_btn = QPushButton("Yenile")
        refresh_btn.clicked.connect(self.refresh_report)
        layout.addWidget(refresh_btn, alignment=Qt.AlignLeft)

        self.report_layout = QVBoxLayout()
        layout.addLayout(self.report_layout)
        layout.addStretch()
        self.refresh_report()

    def refresh_users(self):
        users = User.get_all()
        self.users_table.setRowCount(len(users))
        for i, u in enumerate(users):
            self.users_table.setItem(i, 0, QTableWidgetItem(str(u.id)))
            self.users_table.setItem(i, 1, QTableWidgetItem(u.username))
            self.users_table.setItem(i, 2, QTableWidgetItem(u.email))
            self.users_table.setItem(i, 3, QTableWidgetItem(u.role))
            self.users_table.setItem(i, 4, QTableWidgetItem(str(u.created_at)[:10] if u.created_at else ""))

    def refresh_jobs(self):
        jobs = Job.get_all(active_only=False)
        self.jobs_table.setRowCount(len(jobs))
        for i, job in enumerate(jobs):
            self.jobs_table.setItem(i, 0, QTableWidgetItem(str(job.id)))
            self.jobs_table.setItem(i, 1, QTableWidgetItem(job.title))
            self.jobs_table.setItem(i, 2, QTableWidgetItem(job.company))
            self.jobs_table.setItem(i, 3, QTableWidgetItem(job.location))
            self.jobs_table.setItem(i, 4, QTableWidgetItem("Aktif" if job.is_active else "Pasif"))
            self.jobs_table.setItem(i, 5, QTableWidgetItem(str(job.created_at)[:10] if job.created_at else ""))

    def refresh_report(self):
        while self.report_layout.count():
            item = self.report_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        summary = ReportGenerator.get_summary()
        for key, val in summary.items():
            row = QHBoxLayout()
            lbl = QLabel(f"<b>{key}:</b>")
            val_lbl = QLabel(str(val))
            val_lbl.setStyleSheet("font-size: 18px; font-weight: bold; color: #2563eb;")
            row.addWidget(lbl)
            row.addWidget(val_lbl)
            row.addStretch()
            container = QWidget()
            container.setLayout(row)
            container.setStyleSheet("border: 1px solid #e2e8f0; border-radius: 6px; padding: 8px; background: white;")
            self.report_layout.addWidget(container)

        top_label = QLabel("<b>En Çok Başvuru Alan İlanlar:</b>")
        self.report_layout.addWidget(top_label)
        for r in ReportGenerator.top_jobs():
            lbl = QLabel(f"  • {r['title']} ({r['company']}) → {r['app_count']} başvuru")
            self.report_layout.addWidget(lbl)

    def delete_user(self):
        row = self.users_table.currentRow()
        if row < 0:
            self.show_message("Uyarı", "Lütfen bir kullanıcı seçin.", "warning")
            return
        user_id = int(self.users_table.item(row, 0).text())
        username = self.users_table.item(row, 1).text()
        if self.show_confirm("Sil", f'"{username}" kullanıcısı silinecek. Emin misiniz?'):
            User.delete(user_id)
            self.refresh_users()

    def delete_job(self):
        row = self.jobs_table.currentRow()
        if row < 0:
            self.show_message("Uyarı", "Lütfen bir ilan seçin.", "warning")
            return
        job_id = int(self.jobs_table.item(row, 0).text())
        title = self.jobs_table.item(row, 1).text()
        if self.show_confirm("Sil", f'"{title}" ilanı silinecek. Emin misiniz?'):
            job = Job.get_by_id(job_id)
            if job:
                job.delete()
            self.refresh_jobs()
