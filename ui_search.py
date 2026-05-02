# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_filter.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_searchCard(object):
    def setupUi(self, searchCard):
        if not searchCard.objectName():
            searchCard.setObjectName(u"searchCard")
        searchCard.resize(521, 300)
        searchCard.setStyleSheet(u"#searchCard {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e5e7eb;\n"
"    border-radius: 10px;\n"
"}")
        self.frame = QFrame(searchCard)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 501, 51))
        self.frame.setStyleSheet(u"#searchCard {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #e5e7eb;\n"
"    border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.keyword_input = QLineEdit(self.frame)
        self.keyword_input.setObjectName(u"keyword_input")
        self.keyword_input.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #d1d5db;\n"
"    border-radius: 6px;\n"
"    padding: 6px 10px;\n"
"    background-color: #f9fafb;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid #2563eb;\n"
"    background-color: #ffffff;\n"
"}")

        self.horizontalLayout.addWidget(self.keyword_input)

        self.location_input = QLineEdit(self.frame)
        self.location_input.setObjectName(u"location_input")
        self.location_input.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #d1d5db;\n"
"    border-radius: 6px;\n"
"    padding: 6px 10px;\n"
"    background-color: #f9fafb;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid #2563eb;\n"
"    background-color: #ffffff;\n"
"}")

        self.horizontalLayout.addWidget(self.location_input)

        self.category_combo = QComboBox(self.frame)
        self.category_combo.setObjectName(u"category_combo")
        self.category_combo.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #d1d5db;\n"
"    border-radius: 6px;\n"
"    padding: 5px 8px;\n"
"    background-color: #f9fafb;\n"
"}\n"
"QComboBox:focus {\n"
"    border: 1px solid #2563eb;\n"
"}")

        self.horizontalLayout.addWidget(self.category_combo)

        self.search_btn = QPushButton(self.frame)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: #2563eb;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 6px 14px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #1e40af;\n"
"}")

        self.horizontalLayout.addWidget(self.search_btn)

        self.reset_btn = QPushButton(self.frame)
        self.reset_btn.setObjectName(u"reset_btn")

        self.horizontalLayout.addWidget(self.reset_btn)


        self.retranslateUi(searchCard)

        QMetaObject.connectSlotsByName(searchCard)
    # setupUi

    def retranslateUi(self, searchCard):
        searchCard.setWindowTitle(QCoreApplication.translate("searchCard", u"Form", None))
        self.search_btn.setText(QCoreApplication.translate("searchCard", u"Search", None))
        self.reset_btn.setText(QCoreApplication.translate("searchCard", u"Reset", None))
    # retranslateUi

