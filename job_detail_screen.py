from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QTextEdit, QFrame, QScrollArea, QWidget
)
from PySide6.QtCore import Qt, Signal
from base_widget import BaseWidget
from job import Job
from application import Application
from auth_manager import AuthManager
from notification_manager import NotificationManager


class JobDetailScreen(BaseWidget):
    go_back = Signal()

    def __init__(self, job_id, parent=None):
        super().__init__(parent)
        self.job_id = job_id
        self.job = Job.get_by_id(job_id)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(12)

        back_btn = QPushButton("← Geri")
        back_btn.setFlat(True)
        back_btn.setStyleSheet("color: #2563eb; font-size: 13px;")
        back_btn.clicked.connect(self.go_back.emit)
        layout.addWidget(back_btn, alignment=Qt.AlignLeft)

        if not self.job:
            layout.addWidget(QLabel("İlan bulunamadı."))
            return

        title_lbl = QLabel(self.job.title)
        title_lbl.setStyleSheet("font-size: 22px; font-weight: bold;")
        layout.addWidget(title_lbl)

        company_lbl = QLabel(f"🏢 {self.job.company}")
        company_lbl.setStyleSheet("font-size: 15px; color: #475569;")
        layout.addWidget(company_lbl)

        info_row = QHBoxLayout()
        info_row.addWidget(QLabel(f"📍 {self.job.location}"))
        info_row.addSpacing(20)
        salary = self.job.salary or "Belirtilmemiş"
        info_row.addWidget(QLabel(f"💰 {salary}"))
        info_row.addSpacing(20)
        info_row.addWidget(QLabel(f"📅 {self.job.created_at[:10] if self.job.created_at else ''}"))
        info_row.addStretch()
        layout.addLayout(info_row)

        sep = QFrame()
        sep.setFrameShape(QFrame.HLine)
        sep.setStyleSheet("color: #e2e8f0;")
        layout.addWidget(sep)

        desc_title = QLabel("İlan Açıklaması")
        desc_title.setStyleSheet("font-size: 15px; font-weight: bold;")
        layout.addWidget(desc_title)

        desc_lbl = QLabel(self.job.description or "Açıklama yok.")
        desc_lbl.setWordWrap(True)
        desc_lbl.setStyleSheet("font-size: 13px; color: #334155; line-height: 1.6;")
        layout.addWidget(desc_lbl)

        # Sadece iş arayan görsün
        if AuthManager.is_jobseeker():
            sep2 = QFrame()
            sep2.setFrameShape(QFrame.HLine)
            layout.addWidget(sep2)

            apply_title = QLabel("Başvuru Mektubu (isteğe bağlı)")
            apply_title.setStyleSheet("font-weight: bold;")
            layout.addWidget(apply_title)

            self.cover_letter = QTextEdit()
            self.cover_letter.setPlaceholderText("Kendinizi tanıtın...")
            self.cover_letter.setMaximumHeight(120)
            layout.addWidget(self.cover_letter)

            apply_btn = QPushButton("Başvur")
            apply_btn.setMinimumHeight(38)
            apply_btn.setStyleSheet("background-color: #2563eb; color: white; border-radius: 6px; font-size: 14px;")
            apply_btn.clicked.connect(self.do_apply)
            layout.addWidget(apply_btn)

        layout.addStretch()

    def do_apply(self):
        if not AuthManager.is_logged_in():
            self.show_message("Uyarı", "Başvurmak için giriş yapmalısınız.", "warning")
            return
        cover = self.cover_letter.toPlainText().strip()
        ok, msg = Application.apply(self.job_id, AuthManager.current_user.id, cover)
        if ok:
            NotificationManager.send(
                AuthManager.current_user.id,
                f'"{self.job.title}" ilanına başvurunuz alındı.'
            )
            self.show_message("Başarılı", msg, "success")
        else:
            self.show_message("Hata", msg, "error")
