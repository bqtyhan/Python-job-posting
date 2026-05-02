from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QTableWidgetItem, QHeaderView, QAbstractItemView

from base_widget import BaseWidget
from application import Application, ApplicationStatus
from auth_manager import AuthManager
from ui_application_screen import Ui_Form


class ApplicationScreen(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setup_table()
        self.load_applications()

    # 🔧 Table ayarları (UI üstüne ek)
    def setup_table(self):
        table = self.ui.table

        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setAlternatingRowColors(True)
        table.verticalHeader().setVisible(False)

        # Column genişletme (Job Title + Company)
        table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

    # 📊 Data doldurma
    def load_applications(self):
        table = self.ui.table
        apps = Application.get_by_applicant(AuthManager.current_user.id)

        table.setRowCount(len(apps))

        status_colors = {
            "pending": "#fef3c7",
            "accepted": "#dcfce7",
            "rejected": "#fee2e2"
        }

        for i, row in enumerate(apps):
            table.setItem(i, 0, QTableWidgetItem(str(row["id"])))
            table.setItem(i, 1, QTableWidgetItem(row["job_title"]))
            table.setItem(i, 2, QTableWidgetItem(row["company"]))
            table.setItem(i, 3, QTableWidgetItem(row["applied_at"][:10]))

            status = row["status"]
            status_lbl = ApplicationStatus.LABELS.get(status, status)

            status_item = QTableWidgetItem(status_lbl)
            status_item.setBackground(QColor(status_colors.get(status, "#ffffff")))
            status_item.setTextAlignment(Qt.AlignCenter)

            table.setItem(i, 4, status_item)

        # 🧠 Boş durum
        if not apps:
            table.setRowCount(1)
            empty = QTableWidgetItem("No applications yet.")
            empty.setTextAlignment(Qt.AlignCenter)
            table.setItem(0, 0, empty)
            table.setSpan(0, 0, 1, 5)
