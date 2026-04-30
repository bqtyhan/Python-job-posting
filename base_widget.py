from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Qt


class BaseWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def show_message(self, title, message, msg_type="info"):
        box = QMessageBox(self)
        box.setWindowTitle(title)
        box.setText(message)
        if msg_type == "error":
            box.setIcon(QMessageBox.Critical)
        elif msg_type == "warning":
            box.setIcon(QMessageBox.Warning)
        elif msg_type == "success":
            box.setIcon(QMessageBox.Information)
        else:
            box.setIcon(QMessageBox.Information)
        box.exec()

    def show_confirm(self, title, message):
        reply = QMessageBox.question(
            self, title, message,
            QMessageBox.Yes | QMessageBox.No
        )
        return reply == QMessageBox.Yes

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
