# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'job_listing_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(498, 374)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 16, 5, 16)
        self.lbl_header = QLabel(Form)
        self.lbl_header.setObjectName(u"lbl_header")
        self.lbl_header.setStyleSheet(u"font-size: 20px; font-weight: bold; color: #1e293b;")

        self.verticalLayout_2.addWidget(self.lbl_header)

        self.frame_search = QFrame(Form)
        self.frame_search.setObjectName(u"frame_search")
        self.frame_search.setStyleSheet(u"QLineEdit, QComboBox {\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 6px;\n"
"    padding: 5px 10px;\n"
"    background: white;\n"
"}\n"
"QLineEdit:focus { border-color: #2563eb; }")
        self.frame_search.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_search.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_search)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txt_search = QLineEdit(self.frame_search)
        self.txt_search.setObjectName(u"txt_search")
        self.txt_search.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.txt_search)

        self.txt_location = QLineEdit(self.frame_search)
        self.txt_location.setObjectName(u"txt_location")

        self.horizontalLayout.addWidget(self.txt_location)

        self.combo_category = QComboBox(self.frame_search)
        self.combo_category.addItem("")
        self.combo_category.addItem("")
        self.combo_category.addItem("")
        self.combo_category.addItem("")
        self.combo_category.addItem("")
        self.combo_category.addItem("")
        self.combo_category.addItem("")
        self.combo_category.setObjectName(u"combo_category")

        self.horizontalLayout.addWidget(self.combo_category)

        self.btn_search = QPushButton(self.frame_search)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setStyleSheet(u"QPushButton {\n"
"    background-color: #2563eb;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px 16px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover { background-color: #1d4ed8; }")

        self.horizontalLayout.addWidget(self.btn_search)

        self.btn_reset = QPushButton(self.frame_search)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setStyleSheet(u"QPushButton {\n"
"    background: transparent;\n"
"    color: #64748b;\n"
"    font-weight: 500;\n"
"    border: none;\n"
"}\n"
"QPushButton:hover { color: #1e293b; text-decoration: underline; }")

        self.horizontalLayout.addWidget(self.btn_reset)


        self.verticalLayout_2.addWidget(self.frame_search)

        self.lbl_count = QLabel(Form)
        self.lbl_count.setObjectName(u"lbl_count")
        self.lbl_count.setStyleSheet(u"color: #64748b; \n"
"font-size: 13px;\n"
"margin-left: 2px;")

        self.verticalLayout_2.addWidget(self.lbl_count)

        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea { background-color: transparent; border: none; }\n"
"#scrollAreaWidgetContents { background-color: transparent; }")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.jobs_container = QWidget()
        self.jobs_container.setObjectName(u"jobs_container")
        self.jobs_container.setGeometry(QRect(0, 0, 488, 215))
        self.verticalLayout = QVBoxLayout(self.jobs_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 194, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.jobs_container)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_header.setText(QCoreApplication.translate("Form", u"\u0130\u015f ilanlar\u0131", None))
        self.txt_search.setPlaceholderText(QCoreApplication.translate("Form", u"\u015eirket ara", None))
        self.txt_location.setPlaceholderText(QCoreApplication.translate("Form", u"\u015eehir ara", None))
        self.combo_category.setItemText(0, QCoreApplication.translate("Form", u"Yaz\u0131l\u0131m", None))
        self.combo_category.setItemText(1, QCoreApplication.translate("Form", u"Pazarlama", None))
        self.combo_category.setItemText(2, QCoreApplication.translate("Form", u"Tasar\u0131m", None))
        self.combo_category.setItemText(3, QCoreApplication.translate("Form", u"Muhasebe", None))
        self.combo_category.setItemText(4, QCoreApplication.translate("Form", u"\u0130nsan Kaynaklar\u0131", None))
        self.combo_category.setItemText(5, QCoreApplication.translate("Form", u"Sat\u0131\u015f", None))
        self.combo_category.setItemText(6, QCoreApplication.translate("Form", u"Di\u011fer", None))

        self.combo_category.setPlaceholderText(QCoreApplication.translate("Form", u"Kategoriler", None))
        self.btn_search.setText(QCoreApplication.translate("Form", u"Ara", None))
        self.btn_reset.setText(QCoreApplication.translate("Form", u"S\u0131f\u0131rla", None))
        self.lbl_count.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

