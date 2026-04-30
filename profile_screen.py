from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QTextEdit, QFormLayout
)
from PySide6.QtCore import Qt
from base_widget import BaseWidget
from auth_manager import AuthManager
from job_seeker import JobSeeker
from employer import Employer


class ProfileScreen(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.user = AuthManager.current_user
        self.setup_ui()
        self.load_profile()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(12)

        header = QLabel("Profilim")
        header.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(header)

        info_lbl = QLabel(f"Kullanıcı: {self.user.username} | E-posta: {self.user.email} | Rol: {self.user.role}")
        info_lbl.setStyleSheet("color: gray; font-size: 13px;")
        layout.addWidget(info_lbl)

        form = QFormLayout()
        form.setSpacing(10)

        self.fullname_input = QLineEdit()
        self.fullname_input.setMinimumHeight(34)
        form.addRow("Ad Soyad:", self.fullname_input)

        self.phone_input = QLineEdit()
        self.phone_input.setMinimumHeight(34)
        form.addRow("Telefon:", self.phone_input)

        self.bio_input = QTextEdit()
        self.bio_input.setMaximumHeight(100)
        form.addRow("Hakkımda:", self.bio_input)

        self.skills_input = QLineEdit()
        self.skills_input.setMinimumHeight(34)
        self.skills_input.setPlaceholderText("Python, SQL, Excel...")
        form.addRow("Beceriler:", self.skills_input)

        layout.addLayout(form)

        save_btn = QPushButton("Kaydet")
        save_btn.setMinimumHeight(36)
        save_btn.setStyleSheet("background-color: #16a34a; color: white; border-radius: 6px;")
        save_btn.clicked.connect(self.save_profile)
        layout.addWidget(save_btn, alignment=Qt.AlignLeft)

        layout.addStretch()

    def load_profile(self):
        if AuthManager.is_employer():
            profile = Employer.get_profile(self.user.id)
        else:
            profile = JobSeeker.get_profile(self.user.id)
        self.fullname_input.setText(profile.full_name or "")
        self.phone_input.setText(profile.phone or "")
        self.bio_input.setPlainText(profile.bio or "")
        self.skills_input.setText(profile.skills or "")

    def save_profile(self):
        if AuthManager.is_employer():
            profile = Employer(self.user.id)
        else:
            profile = JobSeeker(self.user.id)
        profile.full_name = self.fullname_input.text().strip()
        profile.phone = self.phone_input.text().strip()
        profile.bio = self.bio_input.toPlainText().strip()
        profile.skills = self.skills_input.text().strip()
        profile.save()
        self.show_message("Başarılı", "Profil güncellendi.", "success")
