from PySide6.QtWidgets import (
    QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem,
    QHeaderView, QFrame
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from base_widget import BaseWidget
from application import Application, ApplicationStatus
from auth_manager import AuthManager


class ApplicationScreen(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.load_applications()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(10)

        header = QLabel("Başvurularım")
        header.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(header)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["#", "İş Başlığı", "Şirket", "Başvuru Tarihi", "Durum"])
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setFrameShape(QFrame.NoFrame)
        layout.addWidget(self.table)

    def load_applications(self):
        apps = Application.get_by_applicant(AuthManager.current_user.id)
        self.table.setRowCount(len(apps))

        status_colors = {
            "pending": "#fef3c7",
            "accepted": "#dcfce7",
            "rejected": "#fee2e2"
        }

        for i, row in enumerate(apps):
            self.table.setItem(i, 0, QTableWidgetItem(str(row["id"])))
            self.table.setItem(i, 1, QTableWidgetItem(row["job_title"]))
            self.table.setItem(i, 2, QTableWidgetItem(row["company"]))
            self.table.setItem(i, 3, QTableWidgetItem(row["applied_at"][:10]))
            status = row["status"]
            status_lbl = ApplicationStatus.LABELS.get(status, status)
            status_item = QTableWidgetItem(status_lbl)
            status_item.setBackground(QColor(status_colors.get(status, "#ffffff")))
            status_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(i, 4, status_item)

        if not apps:
            self.table.setRowCount(1)
            empty = QTableWidgetItem("Henüz başvurunuz yok.")
            empty.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(0, 0, empty)
            self.table.setSpan(0, 0, 1, 5)
