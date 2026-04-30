from PySide6.QtWidgets import (
    QHBoxLayout, QLineEdit, QPushButton, QComboBox, QLabel
)
from PySide6.QtCore import Signal
from base_widget import BaseWidget
from job import JobCategory


class SearchFilterWidget(BaseWidget):
    search_clicked = Signal(str, int, str)  # keyword, category_id, location

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)

        self.keyword_input = QLineEdit()
        self.keyword_input.setPlaceholderText("İş unvanı veya şirket ara...")
        self.keyword_input.setMinimumHeight(34)
        layout.addWidget(self.keyword_input, 3)

        self.location_input = QLineEdit()
        self.location_input.setPlaceholderText("Şehir")
        self.location_input.setMinimumHeight(34)
        layout.addWidget(self.location_input, 1)

        self.category_combo = QComboBox()
        self.category_combo.setMinimumHeight(34)
        self.category_combo.addItem("Tüm Kategoriler", None)
        for cat in JobCategory.get_all():
            self.category_combo.addItem(cat.name, cat.id)
        layout.addWidget(self.category_combo, 1)

        search_btn = QPushButton("Ara")
        search_btn.setMinimumHeight(34)
        search_btn.setStyleSheet("background-color: #2563eb; color: white; border-radius: 5px; padding: 0 14px;")
        search_btn.clicked.connect(self.emit_search)
        layout.addWidget(search_btn)

        reset_btn = QPushButton("Sıfırla")
        reset_btn.setMinimumHeight(34)
        reset_btn.setStyleSheet("border-radius: 5px; padding: 0 10px;")
        reset_btn.clicked.connect(self.reset)
        layout.addWidget(reset_btn)

        self.keyword_input.returnPressed.connect(self.emit_search)

    def emit_search(self):
        keyword = self.keyword_input.text().strip()
        category_id = self.category_combo.currentData()
        location = self.location_input.text().strip()
        self.search_clicked.emit(keyword, category_id or 0, location)

    def reset(self):
        self.keyword_input.clear()
        self.location_input.clear()
        self.category_combo.setCurrentIndex(0)
        self.search_clicked.emit("", 0, "")
