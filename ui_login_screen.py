# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(626, 470)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(150, 70, 256, 234))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 22px; font-weight: bold; margin-bottom: 10px;")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: #2563eb; font-weight: bold;")

        self.verticalLayout.addWidget(self.label_2)

        self.username_input = QLineEdit(self.layoutWidget)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setMinimumSize(QSize(50, 36))

        self.verticalLayout.addWidget(self.username_input)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, 60, -1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.password_input = QLineEdit(self.layoutWidget)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setMinimumSize(QSize(50, 36))

        self.verticalLayout.addWidget(self.password_input)

        self.login_btn = QPushButton(self.layoutWidget)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(0, 38))
        self.login_btn.setStyleSheet(u"background-color: #2563eb; color: white; border-radius: 6px; font-size: 14px;")

        self.verticalLayout.addWidget(self.login_btn)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.reg_btn = QPushButton(self.layoutWidget)
        self.reg_btn.setObjectName(u"reg_btn")

        self.horizontalLayout.addWidget(self.reg_btn)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Job Application System", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Sign in", None))
        self.username_input.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.password_input.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.login_btn.setText(QCoreApplication.translate("Form", u"Sign In", None))
        self.reg_btn.setText(QCoreApplication.translate("Form", u"Sign up", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Dont you have an account?", None))
    # retranslateUi

