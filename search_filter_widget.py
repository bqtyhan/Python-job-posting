from PySide6.QtCore import Signal
from base_widget import BaseWidget
from ui_search import Ui_searchCard
from job import JobCategory


class SearchFilterWidget(BaseWidget):
    search_clicked = Signal(str, int, str)  # keyword, category_id, location

    def __init__(self, parent=None):
        super().__init__(parent)

        # 🔹 Designer UI
        self.ui = Ui_searchCard()
        self.ui.setupUi(self)

        # 🔹 Category doldur
        self.load_categories()

        # 🔹 Bağlantılar
        self.ui.search_btn.clicked.connect(self.emit_search)
        self.ui.reset_btn.clicked.connect(self.reset)
        self.ui.keyword_input.returnPressed.connect(self.emit_search)

    def load_categories(self):
        self.ui.category_combo.clear()
        self.ui.category_combo.addItem("All Categories", 0)

        for cat in JobCategory.get_all():
            self.ui.category_combo.addItem(cat.name, cat.id)

    def emit_search(self):
        keyword = self.ui.keyword_input.text().strip()
        category_id = self.ui.category_combo.currentData()
        location = self.ui.location_input.text().strip()

        self.search_clicked.emit(keyword, category_id or 0, location)

    def reset(self):
        self.ui.keyword_input.clear()
        self.ui.location_input.clear()
        self.ui.category_combo.setCurrentIndex(0)

        self.search_clicked.emit("", 0, "")
