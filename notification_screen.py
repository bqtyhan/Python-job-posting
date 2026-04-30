from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QWidget, QFrame
)
from PySide6.QtCore import Qt
from base_widget import BaseWidget
from auth_manager import AuthManager
from notification_manager import NotificationManager


class NotificationScreen(BaseWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.user = AuthManager.current_user
        self.setup_ui()
        self.load_notifications()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(10)

        header_row = QHBoxLayout()
        header = QLabel("Bildirimler")
        header.setStyleSheet("font-size: 20px; font-weight: bold;")
        header_row.addWidget(header)
        header_row.addStretch()

        mark_all_btn = QPushButton("Tümünü Okundu İşaretle")
        mark_all_btn.setStyleSheet("color: #2563eb; border: none; font-size: 13px;")
        mark_all_btn.clicked.connect(self.mark_all_read)
        header_row.addWidget(mark_all_btn)
        layout.addLayout(header_row)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        self.notif_container = QWidget()
        self.notif_layout = QVBoxLayout(self.notif_container)
        self.notif_layout.setAlignment(Qt.AlignTop)
        self.notif_layout.setSpacing(6)
        scroll.setWidget(self.notif_container)
        layout.addWidget(scroll)

    def load_notifications(self):
        self.clear_layout(self.notif_layout)
        notifs = NotificationManager.get_all(self.user.id)

        if not notifs:
            lbl = QLabel("Henüz hiç bildirim yok.")
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setStyleSheet("color: gray; margin-top: 30px;")
            self.notif_layout.addWidget(lbl)
            return

        for n in notifs:
            card = QFrame()
            card.setFrameShape(QFrame.StyledPanel)
            bg = "#eff6ff" if not n["is_read"] else "#f8fafc"
            card.setStyleSheet(f"border: 1px solid #e2e8f0; border-radius: 6px; background: {bg}; padding: 4px;")
            card_layout = QHBoxLayout(card)

            msg_lbl = QLabel(n["message"])
            msg_lbl.setWordWrap(True)
            card_layout.addWidget(msg_lbl, 1)

            date_lbl = QLabel(str(n["created_at"])[:16])
            date_lbl.setStyleSheet("color: gray; font-size: 11px;")
            card_layout.addWidget(date_lbl)

            if not n["is_read"]:
                mark_btn = QPushButton("✓")
                mark_btn.setStyleSheet("color: #16a34a; border: none; font-size: 14px;")
                mark_btn.setFixedWidth(28)
                mark_btn.clicked.connect(lambda _, nid=n["id"]: self.mark_one(nid))
                card_layout.addWidget(mark_btn)

            self.notif_layout.addWidget(card)

    def mark_one(self, notif_id):
        NotificationManager.mark_read(notif_id)
        self.load_notifications()

    def mark_all_read(self):
        NotificationManager.mark_all_read(self.user.id)
        self.load_notifications()
