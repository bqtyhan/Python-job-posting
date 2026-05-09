from PySide6.QtCore import Signal
from base_widget import BaseWidget
from ui_job_detail import Ui_Form
from job import Job
from application import Application
from auth_manager import AuthManager


class JobDetailScreen(BaseWidget):
    go_back = Signal()

    def __init__(self, job_id, parent=None):
        super().__init__(parent)

        # 🔹 UI yükle
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.job_id = job_id
        self.job = Job.get_by_id(job_id)

        # 🔹 fonksiyonlar
        self.setup_data()
        self.setup_connections()

    def setup_data(self):
        if not self.job:
            self.ui.title_lbl.setText("Job not found")
            return

        self.ui.title_lbl.setText(self.job.title or "-")

        # 🔴 ÖNEMLİ: eski text varsa temizle → placeholder görünsün
        self.ui.cover_letter.clear()
        self.ui.cover_letter.setPlaceholderText(
            "Write your cover letter..."
        )

        self.ui.company_lbl.setText(f"🏢 {self.job.company or '-'}")
        self.ui.location_lbl.setText(f"📍 {self.job.location or '-'}")

        salary = self.job.salary or "Not specified"
        self.ui.salary_lbl.setText(f"💰 {salary}")

        date = (self.job.created_at or "")[:10]
        self.ui.date_lbl.setText(f"📅 {date}" if date else "")

        self.ui.desc_lbl.setText(self.job.description or "No description")
        self.ui.desc_lbl.setWordWrap(True)

    def setup_connections(self):
        self.ui.back_btn.clicked.connect(self.go_back.emit)
        self.ui.apply_btn.clicked.connect(self.do_apply)

    def do_apply(self):
        if not AuthManager.is_logged_in():
            self.show_message("Warning", "You must log in to apply.", "warning")
            return

        cover = self.ui.cover_letter.toPlainText().strip()

        ok, msg = Application.apply(
            self.job_id,
            AuthManager.current_user.id,
            cover
        )

        if ok:
            NotificationManager.send(
                AuthManager.current_user.id,
                f'Your application for "{self.job.title}" has been submitted.'
            )
            self.show_message("Success", msg, "success")
        else:
            self.show_message("Error", msg, "error")
