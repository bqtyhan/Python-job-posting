from PySide6.QtCore import Signal
from base_widget import BaseWidget
from ui_search import Ui_searchCard
from job import JobCategory


class SearchFilterWidget(BaseWidget):
    """Kullanıcıların anahtar kelime, kategori ve konuma göre iş ilanı araması yapmasını sağlayan filtreleme aracı."""

    # Arama butonuna tıklandığında (anahtar kelime, kategori_id, konum) verilerini taşıyan sinyal
    search_clicked = Signal(str, int, str)

    def __init__(self, parent=None):
        """
        Arama filtresi bileşenini başlatır, Designer arayüzünü yükler,
        kategorileri listeye doldurur ve buton bağlantılarını kurar.
        """
        super().__init__(parent)

        # Designer üzerinden gelen kullanıcı arayüzü (UI) kurulumu
        self.ui = Ui_searchCard()
        self.ui.setupUi(self)

        # Veritabanındaki iş kategorilerini seçim kutusuna (ComboBox) yükler
        self.load_categories()

        # Arayüzdeki etkileşimleri ilgili fonksiyonlara bağlar
        self.ui.search_btn.clicked.connect(self.emit_search)
        self.ui.reset_btn.clicked.connect(self.reset)
        # Anahtar kelime alanında Enter tuşuna basıldığında aramayı başlatır
        self.ui.keyword_input.returnPressed.connect(self.emit_search)

    def load_categories(self):
        """
        Sistemdeki tüm iş kategorilerini veritabanından çeker ve
        'Tüm Kategoriler' seçeneği ile birlikte seçim kutusuna ekler.
        """
        self.ui.category_combo.clear()
        self.ui.category_combo.addItem("Tüm Kategoriler", 0)

        # JobCategory modelini kullanarak kategorileri döngüyle ekler
        for cat in JobCategory.get_all():
            self.ui.category_combo.addItem(cat.name, cat.id)

    def emit_search(self):
        """
        Giriş alanlarındaki (kelime, kategori, konum) verileri toplar
        ve bu verileri search_clicked sinyali ile ana ekrana gönderir.
        """
        keyword = self.ui.keyword_input.text().strip()
        category_id = self.ui.category_combo.currentData()
        location = self.ui.location_input.text().strip()

        # Sinyali verilerle birlikte yayınlar
        self.search_clicked.emit(keyword, category_id or 0, location)

    def reset(self):
        """
        Tüm filtreleme alanlarını temizler, kategori seçimini başa döndürür
        ve boş bir arama sinyali göndererek listeyi sıfırlar.
        """
        self.ui.keyword_input.clear()
        self.ui.location_input.clear()
        self.ui.category_combo.setCurrentIndex(0)

        # Filtreleri sıfırladıktan sonra listeyi güncellemek için boş sinyal gönderir
        self.search_clicked.emit("", 0, "")