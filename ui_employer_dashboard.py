# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employer_dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        Form.setStyleSheet(u"/* Genel Arka Plan ve Yaz\u0131 */\n"
"QWidget {\n"
"    background-color: #f8fafc;\n"
"    font-family: 'Segoe UI', sans-serif;\n"
"    color: #1e293b;\n"
"}\n"
"\n"
"/* Tablo Tasar\u0131m\u0131 */\n"
"QTableWidget {\n"
"    background-color: white;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    gridline-color: transparent; /* Izgara \u00e7izgilerini gizle */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f1f5f9;\n"
"    padding: 8px;\n"
"    border: none;\n"
"    border-bottom: 2px solid #e2e8f0;\n"
"    font-weight: bold;\n"
"    color: #64748b;\n"
"}\n"
"\n"
"/* Butonlar */\n"
"#btn_add_job {\n"
"    background-color: #16a34a; /* Ye\u015fil */\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 8px 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#btn_accept {\n"
"    background-color: #2563eb; /* Mavi */\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px 14px;\n"
"}\n"
"\n"
"#btn_reject {\n"
"    background-color: #dc2626; /* K\u0131"
                        "rm\u0131z\u0131 */\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px 14px;\n"
"}\n"
"\n"
"/* Tab Sayfalar\u0131 */\n"
"QTabWidget::pane {\n"
"    border: 1px solid #e2e8f0;\n"
"    background: white;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: #f1f5f9;\n"
"    padding: 10px 20px;\n"
"    border-top-left-radius: 8px;\n"
"    border-top-right-radius: 8px;\n"
"    margin-right: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"    border-bottom: 2px solid #2563eb;\n"
"    font-weight: bold;\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_header = QLabel(Form)
        self.lbl_header.setObjectName(u"lbl_header")
        self.lbl_header.setStyleSheet(u"#lbl_header {\n"
"    color: #0f172a; /* \u00c7ok koyu, premium bir ton */\n"
"    font-size: 15px; /* Ba\u015fl\u0131k oldu\u011fu uzaktan belli olsun */\n"
"    font-weight: 800; /* Ekstra kal\u0131n font */\n"
"    letter-spacing: -0.5px; /* Harfleri biraz yakla\u015ft\u0131rarak modern bir hava verdik */\n"
"    padding: 5px 0px; /* \u00dcstten ve alttan biraz bo\u015fluk */\n"
"    /* Alt\u0131na \u00e7ok hafif, modern bir \u00e7izgi ekleyerek ay\u0131r\u0131yoruz */\n"
"    border-bottom: 2px solid #e2e8f0; \n"
"    margin-bottom: 5px;\n"
"}")

        self.verticalLayout.addWidget(self.lbl_header)

        self.tabs = QTabWidget(Form)
        self.tabs.setObjectName(u"tabs")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_add_job = QPushButton(self.tab)
        self.btn_add_job.setObjectName(u"btn_add_job")

        self.horizontalLayout_2.addWidget(self.btn_add_job)

        self.horizontalSpacer = QSpacerItem(268, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.jobs_table = QTableWidget(self.tab)
        if (self.jobs_table.columnCount() < 6):
            self.jobs_table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.jobs_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.jobs_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.jobs_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.jobs_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.jobs_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.jobs_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.jobs_table.setObjectName(u"jobs_table")
        self.jobs_table.setAlternatingRowColors(True)
        self.jobs_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.jobs_table.setShowGrid(False)
        self.jobs_table.setColumnCount(6)
        self.jobs_table.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.jobs_table)

        self.tabs.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.apps_table = QTableWidget(self.tab_2)
        if (self.apps_table.columnCount() < 6):
            self.apps_table.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.apps_table.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.apps_table.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.apps_table.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.apps_table.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.apps_table.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.apps_table.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        self.apps_table.setObjectName(u"apps_table")
        self.apps_table.setAlternatingRowColors(True)
        self.apps_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.apps_table.setShowGrid(False)
        self.apps_table.setColumnCount(6)
        self.apps_table.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.apps_table)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_accept = QPushButton(self.tab_2)
        self.btn_accept.setObjectName(u"btn_accept")

        self.horizontalLayout_3.addWidget(self.btn_accept)

        self.btn_reject = QPushButton(self.tab_2)
        self.btn_reject.setObjectName(u"btn_reject")

        self.horizontalLayout_3.addWidget(self.btn_reject)

        self.horizontalSpacer_2 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.tabs.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabs)


        self.retranslateUi(Form)

        self.tabs.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_header.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.btn_add_job.setText(QCoreApplication.translate("Form", u"+ Yeni \u0130lan Ekle", None))
        ___qtablewidgetitem = self.jobs_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None))
        ___qtablewidgetitem1 = self.jobs_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Ba\u015fl\u0131k", None))
        ___qtablewidgetitem2 = self.jobs_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u015eirket", None))
        ___qtablewidgetitem3 = self.jobs_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Konum", None))
        ___qtablewidgetitem4 = self.jobs_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Durum", None))
        ___qtablewidgetitem5 = self.jobs_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\u0130\u015flem", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab), QCoreApplication.translate("Form", u"\u0130lanlar\u0131m", None))
        ___qtablewidgetitem6 = self.apps_table.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"ID", None))
        ___qtablewidgetitem7 = self.apps_table.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"\u0130lan", None))
        ___qtablewidgetitem8 = self.apps_table.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Ba\u015fvuran", None))
        ___qtablewidgetitem9 = self.apps_table.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"E-posta", None))
        ___qtablewidgetitem10 = self.apps_table.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"Tarih", None))
        ___qtablewidgetitem11 = self.apps_table.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"Durum", None))
        self.btn_accept.setText(QCoreApplication.translate("Form", u"Kabul et", None))
        self.btn_reject.setText(QCoreApplication.translate("Form", u"Reddet", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Ba\u015fvurular", None))
    # retranslateUi

