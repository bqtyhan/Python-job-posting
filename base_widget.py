from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Qt


class BaseWidget(QWidget):
    """Diğer tüm pencere ve widget'lar için ortak kullanılan temel yardımcı metotları içeren sınıf."""

    def __init__(self, parent=None):
        """Widget bileşenini başlatır ve varsa üst (parent) bileşenine bağlar."""
        super().__init__(parent)

    def show_message(self, title, message, msg_type="info"):
        """
        Kullanıcıya bilgi, uyarı veya hata mesajı göstermek için standart bir mesaj kutusu açar.

        Args:
            title (str): Mesaj kutusunun başlığı.
            message (str): Gösterilecek olan mesaj metni.
            msg_type (str): Mesajın tipi ("error", "warning", "success" veya "info").
        """
        box = QMessageBox(self)
        box.setWindowTitle(title)
        box.setText(message)

        # Mesaj tipine göre uygun simgeyi (icon) belirler
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
        """
        Kullanıcıdan bir işlem için onay (Evet/Hayır) isteyen bir diyalog penceresi açar.

        Args:
            title (str): Onay penceresinin başlığı.
            message (str): Kullanıcıya sorulacak soru metni.

        Returns:
            bool: Kullanıcı 'Evet' seçeneğine tıklarsa True, aksi halde False döner.
        """
        reply = QMessageBox.question(
            self, title, message,
            QMessageBox.Yes | QMessageBox.No
        )
        return reply == QMessageBox.Yes

    def clear_layout(self, layout):
        """
        Verilen bir layout (düzenleyici) içerisindeki tüm widget'ları ve bileşenleri temizler.
        Genellikle listelerin veya içeriklerin dinamik olarak güncellenmesi öncesinde kullanılır.

        Args:
            layout (QLayout): Temizlenecek olan düzenleyici nesnesi.
        """
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                # Widget'ı güvenli bir şekilde bellekten siler
                widget.deleteLater()
