from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QScrollArea, QWidget, QFrame
)
from PySide6.QtCore import Qt, Signal
from base_widget import BaseWidget
from job import Job
from search_filter_widget import SearchFilterWidget


class JobCard(QFrame):
    clicked = Signal(int)

    def __init__(self, job, parent=None):
        super().__init__(parent)
        self.job = job
        self.setFrameShape(QFrame.StyledPanel)
        self.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet("""
            QFrame { border: 1px solid #e2e8f0; border-radius: 8px; background: white; }
            QFrame:hover { border-color: #2563eb; background: #f0f7ff; }
        """)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(14, 10, 14, 10)
        layout.setSpacing(4)

        top = QHBoxLayout()
        title_lbl = QLabel(job.title)
        title_lbl.setStyleSheet("font-size: 15px; font-weight: bold; color: #1e293b;")
        top.addWidget(title_lbl)
        top.addStretch()
        date_lbl = QLabel(job.created_at[:10] if job.created_at else "")
        date_lbl.setStyleSheet("color: gray; font-size: 12px;")
        top.addWidget(date_lbl)
        layout.addLayout(top)

        company_lbl = QLabel(f"🏢 {job.company}")
        company_lbl.setStyleSheet("color: #475569;")
        layout.addWidget(company_lbl)

        info = QHBoxLayout()
        info.addWidget(QLabel(f"📍 {job.location}"))
        info.addSpacing(16)
        salary_text = job.salary if job.salary else "Belirtilmemiş"
        info.addWidget(QLabel(f"💰 {salary_text}"))
        info.addStretch()
        layout.addLayout(info)

    def mousePressEvent(self, event):
        self.clicked.emit(self.job.id)


class JobListingScreen(BaseWidget):
    job_selected = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.load_jobs()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(10)

        header = QLabel("İş İlanları")
        header.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(header)

        self.search_widget = SearchFilterWidget()
        self.search_widget.search_clicked.connect(self.do_search)
        layout.addWidget(self.search_widget)

        self.count_label = QLabel("")
        self.count_label.setStyleSheet("color: gray; font-size: 13px;")
        layout.addWidget(self.count_label)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        self.jobs_container = QWidget()
        self.jobs_layout = QVBoxLayout(self.jobs_container)
        self.jobs_layout.setAlignment(Qt.AlignTop)
        self.jobs_layout.setSpacing(8)
        scroll.setWidget(self.jobs_container)
        layout.addWidget(scroll)

    def load_jobs(self, jobs=None):
        if jobs is None:
            jobs = Job.get_all()
        self.clear_layout(self.jobs_layout)
        self.count_label.setText(f"{len(jobs)} ilan bulundu")

        if not jobs:
            lbl = QLabel("Hiç ilan bulunamadı.")
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setStyleSheet("color: gray; margin-top: 40px; font-size: 14px;")
            self.jobs_layout.addWidget(lbl)
            return

        for job in jobs:
            card = JobCard(job)
            card.clicked.connect(self.job_selected.emit)
            self.jobs_layout.addWidget(card)

    def do_search(self, keyword, category_id, location):
        results = Job.search(keyword, category_id if category_id else None, location)
        self.load_jobs(results)
