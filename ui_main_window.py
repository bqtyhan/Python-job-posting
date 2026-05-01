# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(742, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_menu_frame = QFrame(self.centralwidget)
        self.left_menu_frame.setObjectName(u"left_menu_frame")
        self.left_menu_frame.setMinimumSize(QSize(200, 0))
        self.left_menu_frame.setMaximumSize(QSize(200, 16777215))
        self.left_menu_frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.left_menu_frame.setStyleSheet(u"background-color: #1e293b;\n"
"")
        self.left_menu_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.left_menu_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.left_menu_frame)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_logo = QLabel(self.left_menu_frame)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setStyleSheet(u"color: white;\n"
"font-size: 15px;\n"
"font-weight: bold;\n"
"padding: 10px;")

        self.verticalLayout.addWidget(self.lbl_logo)

        self.lbl_username = QLabel(self.left_menu_frame)
        self.lbl_username.setObjectName(u"lbl_username")
        self.lbl_username.setStyleSheet(u"color: #94a3b8;\n"
"font-size: 12px;\n"
"padding: 10px;")

        self.verticalLayout.addWidget(self.lbl_username)

        self.btn_jobs = QPushButton(self.left_menu_frame)
        self.btn_jobs.setObjectName(u"btn_jobs")
        self.btn_jobs.setStyleSheet(u"QPushButton {\n"
"    color: #cbd5e1; \n"
"    background: transparent; \n"
"    border: none;\n"
"    text-align: left; \n"
"    padding: 12px 18px; \n"
"    font-size: 13px;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: #334155; \n"
"    color: white; \n"
"}")
        self.btn_jobs.setFlat(True)

        self.verticalLayout.addWidget(self.btn_jobs)

        self.btn_apps = QPushButton(self.left_menu_frame)
        self.btn_apps.setObjectName(u"btn_apps")
        self.btn_apps.setStyleSheet(u"QPushButton {\n"
"    color: #cbd5e1; \n"
"    background: transparent; \n"
"    border: none;\n"
"    text-align: left; \n"
"    padding: 12px 18px; \n"
"    font-size: 13px;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: #334155; \n"
"    color: white; \n"
"}")
        self.btn_apps.setFlat(True)

        self.verticalLayout.addWidget(self.btn_apps)

        self.btn_employer = QPushButton(self.left_menu_frame)
        self.btn_employer.setObjectName(u"btn_employer")
        self.btn_employer.setStyleSheet(u"QPushButton {\n"
"    color: #cbd5e1; \n"
"    background: transparent; \n"
"    border: none;\n"
"    text-align: left; \n"
"    padding: 12px 18px; \n"
"    font-size: 13px;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: #334155; \n"
"    color: white; \n"
"}")
        self.btn_employer.setFlat(True)

        self.verticalLayout.addWidget(self.btn_employer)

        self.btn_admin = QPushButton(self.left_menu_frame)
        self.btn_admin.setObjectName(u"btn_admin")
        self.btn_admin.setStyleSheet(u"QPushButton {\n"
"    color: #cbd5e1; \n"
"    background: transparent; \n"
"    border: none;\n"
"    text-align: left; \n"
"    padding: 12px 18px; \n"
"    font-size: 13px;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: #334155; \n"
"    color: white; \n"
"}")
        self.btn_admin.setFlat(True)

        self.verticalLayout.addWidget(self.btn_admin)

        self.verticalSpacer = QSpacerItem(20, 161, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_logout = QPushButton(self.left_menu_frame)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setStyleSheet(u"QPushButton {\n"
"    color: #f87171; \n"
"}\n"
"QPushButton:hover { \n"
"    background-color: #450a0a; \n"
"}")
        self.btn_logout.setFlat(True)

        self.verticalLayout.addWidget(self.btn_logout)


        self.horizontalLayout.addWidget(self.left_menu_frame)

        self.main_pages = QStackedWidget(self.centralwidget)
        self.main_pages.setObjectName(u"main_pages")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.main_pages.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.main_pages.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.main_pages)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_logo.setText(QCoreApplication.translate("MainWindow", u"\U0001f5c2 \U00000130\U0000015f \U00000130lan Sistemi", None))
        self.lbl_username.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_jobs.setText(QCoreApplication.translate("MainWindow", u"\U0001f50d \U00000130lanlar\U00000131 G\U000000f6zat", None))
        self.btn_apps.setText(QCoreApplication.translate("MainWindow", u"\U0001f4cb Ba\U0000015fvurular\U00000131m", None))
        self.btn_employer.setText(QCoreApplication.translate("MainWindow", u"\U0001f3e2 \U00000130\U0000015fveren Paneli", None))
        self.btn_admin.setText(QCoreApplication.translate("MainWindow", u"\u2699\ufe0f Admin Paneli", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"\U0001f6aa \U000000c7\U00000131k\U00000131\U0000015f Yap", None))
    # retranslateUi

