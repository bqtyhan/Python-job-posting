from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QTableWidget, QTableWidgetItem, QHeaderView,
    QDialog, QFormLayout, QLineEdit, QTextEdit,
    QComboBox, QFrame, QTabWidget, QWidget
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from base_widget import BaseWidget
from job import Job, JobCategory
from application import Application, ApplicationStatus
from auth_manager import AuthManager
from notification_manager import NotificationManager
from database import db


class AddJobDialog(QDialog):
    def __init__(self, parent=None, job=None):
        super().__init__(parent)
        self.job = job
        self.setWindowTitle("İlan Düzenle" if job else "Yeni İlan Ekle")
        self.setMinimumWidth(450)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        form = QFormLayout()
        form.setSpacing(10)

        self.title_input = QLineEdit()
        self.title_input.setMinimumHeight(34)
        form.addRow("İş Başlığı:", self.title_input)

        self.company_input = QLineEdit()
        self.company_input.setMinimumHeight(34)
        form.addRow("Şirket:", self.company_input)

        self.location_input = QLineEdit()
        self.location_input.setMinimumHeight(34)
        form.addRow("Konum:", self.location_input)

        self.salary_input = QLineEdit()
        self.salary_input.setMinimumHeight(34)
        form.addRow("Maaş (isteğe bağlı):", self.salary_input)

        self.category_combo = QComboBox()
        self.category_combo.setMinimumHeight(34)
        for cat in JobCategory.get_all():
            self.category_combo.addItem(cat.name, cat.id)
        form.addRow("Kategori:", self.category_combo)

        self.desc_input = QTextEdit()
        self.desc_input.setMaximumHeight(120)
        form.addRow("Açıklama:", self.desc_input)

        layout.addLayout(form)

        if self.job:
            self.title_input.setText(self.job.title)
            self.company_input.setText(self.job.company)
            self.location_input.setText(self.job.location)
            self.salary_input.setText(self.job.salary or "")
            self.desc_input.setPlainText(self.job.description or "")
            for i in range(self.category_combo.count()):
                if self.category_combo.itemData(i) == self.job.category_id:
                    self.category_combo.setCurrentIndex(i)
                    break

        btn_layout = QHBoxLayout()
        save_btn = QPushButton("Kaydet")
        save_btn.setStyleSheet("background-color: #2563eb; color: white; border-radius: 5px; padding: 6px 20px;")
        save_btn.clicked.connect(self.accept)
        cancel_btn = QPushButton("İptal")
        cancel_btn.clicked.connect(self.reject)
        btn_layout.addStretch()
        btn_layout.addWidget(cancel_btn)
        btn_layout.addWidget(save_btn)
        layout.addLayout(btn_layout)

    def get_data(self):
        return {
            "title": self.title_input.text().strip(),
            "company": self.company_input.text().strip(),
            "location": self.location_input.text().strip(),
            "salary": self.salary_input.text().strip(),
            "category_id": self.category_combo.currentData(),
            "description": self.desc_input.toPlainText().strip()
        }


class EmployerDashboard(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.user = AuthManager.current_user
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)

        header = QLabel(f"İşveren Paneli — {self.user.username}")
        header.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(header)

        tabs = QTabWidget()

        # Tab 1: İlanlarım
        self.jobs_tab = QWidget()
        self.setup_jobs_tab()
        tabs.addTab(self.jobs_tab, "İlanlarım")

        # Tab 2: Başvurular
        self.apps_tab = QWidget()
        self.setup_apps_tab()
        tabs.addTab(self.apps_tab, "Başvurular")

        layout.addWidget(tabs)

    def setup_jobs_tab(self):
        layout = QVBoxLayout(self.jobs_tab)
        layout.setSpacing(8)

        btn_row = QHBoxLayout()
        add_btn = QPushButton("+ Yeni İlan Ekle")
        add_btn.setStyleSheet("background-color: #16a34a; color: white; border-radius: 5px; padding: 6px 14px;")
        add_btn.clicked.connect(self.add_job)
        btn_row.addWidget(add_btn)
        btn_row.addStretch()
        layout.addLayout(btn_row)

        self.jobs_table = QTableWidget()
        self.jobs_table.setColumnCount(6)
        self.jobs_table.setHorizontalHeaderLabels(["ID", "Başlık", "Şirket", "Konum", "Durum", "İşlem"])
        self.jobs_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.jobs_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.jobs_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.jobs_table.setAlternatingRowColors(True)
        self.jobs_table.verticalHeader().setVisible(False)
        self.jobs_table.setFrameShape(QFrame.NoFrame)
        layout.addWidget(self.jobs_table)
        self.refresh_jobs()

    def setup_apps_tab(self):
        layout = QVBoxLayout(self.apps_tab)

        self.apps_table = QTableWidget()
        self.apps_table.setColumnCount(6)
        self.apps_table.setHorizontalHeaderLabels(["ID", "İlan", "Başvuran", "E-posta", "Tarih", "Durum"])
        self.apps_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.apps_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.apps_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.apps_table.setAlternatingRowColors(True)
        self.apps_table.verticalHeader().setVisible(False)
        self.apps_table.setFrameShape(QFrame.NoFrame)
        layout.addWidget(self.apps_table)

        btn_row = QHBoxLayout()
        accept_btn = QPushButton("Kabul Et")
        accept_btn.setStyleSheet("background-color: #16a34a; color: white; border-radius: 5px; padding: 5px 14px;")
        accept_btn.clicked.connect(lambda: self.change_app_status("accepted"))
        reject_btn = QPushButton("Reddet")
        reject_btn.setStyleSheet("background-color: #dc2626; color: white; border-radius: 5px; padding: 5px 14px;")
        reject_btn.clicked.connect(lambda: self.change_app_status("rejected"))
        btn_row.addWidget(accept_btn)
        btn_row.addWidget(reject_btn)
        btn_row.addStretch()
        layout.addLayout(btn_row)

        self.refresh_apps()

    def refresh_jobs(self):
        jobs = Job.get_by_employer(self.user.id)
        self.jobs_table.setRowCount(len(jobs))
        for i, job in enumerate(jobs):
            self.jobs_table.setItem(i, 0, QTableWidgetItem(str(job.id)))
            self.jobs_table.setItem(i, 1, QTableWidgetItem(job.title))
            self.jobs_table.setItem(i, 2, QTableWidgetItem(job.company))
            self.jobs_table.setItem(i, 3, QTableWidgetItem(job.location))
            durum = "Aktif" if job.is_active else "Pasif"
            status_item = QTableWidgetItem(durum)
            status_item.setForeground(QColor("#16a34a") if job.is_active else QColor("#dc2626"))
            self.jobs_table.setItem(i, 4, status_item)

            del_btn = QPushButton("Sil")
            del_btn.setStyleSheet("color: #dc2626; border: none;")
            del_btn.clicked.connect(lambda _, j=job: self.delete_job(j))
            self.jobs_table.setCellWidget(i, 5, del_btn)

    def refresh_apps(self):
        jobs = Job.get_by_employer(self.user.id)
        all_apps = []
        for job in jobs:
            for app in Application.get_by_job(job.id):
                all_apps.append((job, app))

        self.apps_table.setRowCount(len(all_apps))
        status_colors = {"pending": "#fef3c7", "accepted": "#dcfce7", "rejected": "#fee2e2"}

        for i, (job, app) in enumerate(all_apps):
            self.apps_table.setItem(i, 0, QTableWidgetItem(str(app["id"])))
            self.apps_table.setItem(i, 1, QTableWidgetItem(job.title))
            self.apps_table.setItem(i, 2, QTableWidgetItem(app["username"]))
            self.apps_table.setItem(i, 3, QTableWidgetItem(app["email"]))
            self.apps_table.setItem(i, 4, QTableWidgetItem(str(app["applied_at"])[:10]))
            from application import ApplicationStatus
            status_item = QTableWidgetItem(ApplicationStatus.LABELS.get(app["status"], app["status"]))
            status_item.setBackground(QColor(status_colors.get(app["status"], "#fff")))
            status_item.setTextAlignment(Qt.AlignCenter)
            self.apps_table.setItem(i, 5, status_item)

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
        row = self.apps_table.currentRow()
        if row < 0:
            self.show_message("Uyarı", "Lütfen bir başvuru seçin.", "warning")
            return
        app_id = int(self.apps_table.item(row, 0).text())
        Application.update_status(app_id, new_status)
        app = Application.get_by_id(app_id)
        if app:
            msg = "Başvurunuz kabul edildi!" if new_status == "accepted" else "Başvurunuz reddedildi."
            NotificationManager.send(app.applicant_id, msg)
        self.refresh_apps()
