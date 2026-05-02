# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'job_detail.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(477, 365)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.back_btn = QPushButton(Form)
        self.back_btn.setObjectName(u"back_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_btn.sizePolicy().hasHeightForWidth())
        self.back_btn.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(161, 161, 161, 179))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush)
        self.back_btn.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.back_btn.setFont(font)

        self.verticalLayout.addWidget(self.back_btn)

        self.title_lbl = QLabel(Form)
        self.title_lbl.setObjectName(u"title_lbl")

        self.verticalLayout.addWidget(self.title_lbl)

        self.company_lbl = QLabel(Form)
        self.company_lbl.setObjectName(u"company_lbl")

        self.verticalLayout.addWidget(self.company_lbl)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.location_lbl = QLabel(Form)
        self.location_lbl.setObjectName(u"location_lbl")

        self.horizontalLayout.addWidget(self.location_lbl)

        self.salary_lbl = QLabel(Form)
        self.salary_lbl.setObjectName(u"salary_lbl")

        self.horizontalLayout.addWidget(self.salary_lbl)

        self.date_lbl = QLabel(Form)
        self.date_lbl.setObjectName(u"date_lbl")

        self.horizontalLayout.addWidget(self.date_lbl)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.HLine)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame)

        self.desc_title = QLabel(Form)
        self.desc_title.setObjectName(u"desc_title")

        self.verticalLayout.addWidget(self.desc_title)

        self.desc_lbl = QLabel(Form)
        self.desc_lbl.setObjectName(u"desc_lbl")
        self.desc_lbl.setWordWrap(True)

        self.verticalLayout.addWidget(self.desc_lbl)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.HLine)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_2)

        self.cover_title = QLabel(Form)
        self.cover_title.setObjectName(u"cover_title")

        self.verticalLayout.addWidget(self.cover_title)

        self.cover_letter = QTextEdit(Form)
        self.cover_letter.setObjectName(u"cover_letter")

        self.verticalLayout.addWidget(self.cover_letter)

        self.apply_btn = QPushButton(Form)
        self.apply_btn.setObjectName(u"apply_btn")
        palette1 = QPalette()
        brush1 = QBrush(QColor(166, 166, 166, 179))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        self.apply_btn.setPalette(palette1)
        self.apply_btn.setFont(font)

        self.verticalLayout.addWidget(self.apply_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.back_btn.setText(QCoreApplication.translate("Form", u"Back Button", None))
        self.title_lbl.setText(QCoreApplication.translate("Form", u"Title", None))
        self.company_lbl.setText(QCoreApplication.translate("Form", u"Company", None))
        self.location_lbl.setText(QCoreApplication.translate("Form", u"Location", None))
        self.salary_lbl.setText(QCoreApplication.translate("Form", u"Salary", None))
        self.date_lbl.setText(QCoreApplication.translate("Form", u"Date", None))
        self.desc_title.setText(QCoreApplication.translate("Form", u"Description Title", None))
        self.desc_lbl.setText(QCoreApplication.translate("Form", u"Description Text", None))
        self.cover_title.setText(QCoreApplication.translate("Form", u"Cover Letter (optional)", None))
        self.cover_letter.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Cover Letter Input</p></body></html>", None))
        self.apply_btn.setText(QCoreApplication.translate("Form", u"Apply", None))
    # retranslateUi

