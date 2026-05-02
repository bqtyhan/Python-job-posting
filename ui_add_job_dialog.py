# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_job_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QHBoxLayout, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_AddJobDialog(object):
    def setupUi(self, AddJobDialog):
        if not AddJobDialog.objectName():
            AddJobDialog.setObjectName(u"AddJobDialog")
        AddJobDialog.resize(400, 310)
        AddJobDialog.setStyleSheet(u"/* Genel Ayarlar */\n"
"QWidget {\n"
"    background-color: #f8fafc;\n"
"    font-family: 'Segoe UI', sans-serif;\n"
"}\n"
"\n"
"/* Giri\u015f Alanlar\u0131 */\n"
"QLineEdit, QTextEdit, QComboBox {\n"
"    border: 1px solid #cbd5e1;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus, QComboBox:focus {\n"
"    border: 2px solid #3b82f6; /* Odaklan\u0131nca mavi kenarl\u0131k */\n"
"}\n"
"\n"
"/* Kaydet Butonu (Mavi) */\n"
"#btn_save {\n"
"    background-color: #2563eb;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 8px 24px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#btn_save:hover {\n"
"    background-color: #1d4ed8;\n"
"}\n"
"\n"
"/* \u0130ptal Butonu (Gri/Beyaz) */\n"
"#btn_cancel {\n"
"    background-color: #f1f5f9;\n"
"    color: #475569;\n"
"    border: 1px solid #cbd5e1;\n"
"    border-radius: 6px;\n"
"    padding: 8px 20px;\n"
"}\n"
"\n"
"#btn_cancel:hover {\n"
"    background-color: #e2e8f0;\n"
"}")
        self.verticalLayout = QVBoxLayout(AddJobDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.txt_title = QLineEdit(AddJobDialog)
        self.txt_title.setObjectName(u"txt_title")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.txt_title)

        self.txt_company = QLineEdit(AddJobDialog)
        self.txt_company.setObjectName(u"txt_company")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.txt_company)

        self.txt_location = QLineEdit(AddJobDialog)
        self.txt_location.setObjectName(u"txt_location")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.txt_location)

        self.txt_salary = QLineEdit(AddJobDialog)
        self.txt_salary.setObjectName(u"txt_salary")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.txt_salary)

        self.combo_category = QComboBox(AddJobDialog)
        self.combo_category.setObjectName(u"combo_category")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.combo_category)

        self.txt_description = QPlainTextEdit(AddJobDialog)
        self.txt_description.setObjectName(u"txt_description")
        self.txt_description.setStyleSheet(u"#txt_description {\n"
"    background-color: white;\n"
"    border: 1px solid #cbd5e1;\n"
"    border-radius: 6px;\n"
"    /* Metnin kenarlara yap\u0131\u015fmamas\u0131 i\u00e7in ferah bir alan b\u0131rak\u0131yoruz */\n"
"    padding: 8px 10px; \n"
"    color: #1e293b;\n"
"    font-family: 'Segoe UI', sans-serif;\n"
"    font-size: 13px;\n"
"    /* Kutunun \u00e7ok ezilmemesi i\u00e7in en az bir y\u00fckseklik veriyoruz */\n"
"    min-height: 100px; \n"
"}\n"
"\n"
"/* Kutuya t\u0131kland\u0131\u011f\u0131nda (Odaklan\u0131nca) mavi \u00e7er\u00e7eve olsun */\n"
"#txt_description:focus {\n"
"    border: 2px solid #3b82f6;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"/* E\u011fer placeholder rengi \u00e7ok s\u00f6n\u00fckse bunu ekleyebilirsin */\n"
"QPlainTextEdit {\n"
"    color: #1e293b;\n"
"}")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.txt_description)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(208, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_cancel = QPushButton(AddJobDialog)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_save = QPushButton(AddJobDialog)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout.addWidget(self.btn_save)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(AddJobDialog)

        QMetaObject.connectSlotsByName(AddJobDialog)
    # setupUi

    def retranslateUi(self, AddJobDialog):
        AddJobDialog.setWindowTitle(QCoreApplication.translate("AddJobDialog", u"Yeni \u0130lan Ekle", None))
        self.txt_title.setPlaceholderText(QCoreApplication.translate("AddJobDialog", u"\u0130\u015f ba\u015fl\u0131\u011f\u0131", None))
        self.txt_company.setPlaceholderText(QCoreApplication.translate("AddJobDialog", u"\u015eirket", None))
        self.txt_location.setPlaceholderText(QCoreApplication.translate("AddJobDialog", u"Konum", None))
        self.txt_salary.setPlaceholderText(QCoreApplication.translate("AddJobDialog", u"Maa\u015f", None))
        self.combo_category.setPlaceholderText(QCoreApplication.translate("AddJobDialog", u"Kategori", None))
        self.txt_description.setPlaceholderText(QCoreApplication.translate("AddJobDialog", u"A\u00e7\u0131klama", None))
        self.btn_cancel.setText(QCoreApplication.translate("AddJobDialog", u"\u0130ptal", None))
        self.btn_save.setText(QCoreApplication.translate("AddJobDialog", u"Kaydet", None))
    # retranslateUi

