# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_panel.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        Form.setStyleSheet(u"/* Genel Arka Plan */\n"
"QWidget {\n"
"    background-color: #f8fafc;\n"
"    font-family: 'Segoe UI', sans-serif;\n"
"}\n"
"\n"
"/* Admin Paneli Ba\u015fl\u0131\u011f\u0131 */\n"
"#lbl_header {\n"
"    font-size: 22px;\n"
"    font-weight: 800;\n"
"    color: #0f172a;\n"
"    padding: 10px 0px;\n"
"    border-bottom: 2px solid #e2e8f0;\n"
"}\n"
"\n"
"/* Tablolar */\n"
"QTableWidget {\n"
"    background-color: white;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    gridline-color: #f1f5f9;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f8fafc;\n"
"    padding: 8px;\n"
"    border: none;\n"
"    border-bottom: 1px solid #e2e8f0;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* K\u0131rm\u0131z\u0131 Silme Butonlar\u0131 */\n"
"#btn_delete_user, #btn_delete_job {\n"
"    background-color: #dc2626;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 8px 16px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#btn_delete_user:hover, #btn_delete_job:hover {\n"
"    backgr"
                        "ound-color: #b91c1c;\n"
"}\n"
"\n"
"/* Mavi Yenile Butonu */\n"
"#btn_refresh_report {\n"
"    background-color: #2563eb;\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    padding: 8px 20px;\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_header = QLabel(Form)
        self.lbl_header.setObjectName(u"lbl_header")

        self.verticalLayout.addWidget(self.lbl_header)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_users = QWidget()
        self.tab_users.setObjectName(u"tab_users")
        self.verticalLayout_2 = QVBoxLayout(self.tab_users)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.users_table = QTableWidget(self.tab_users)
        if (self.users_table.columnCount() < 5):
            self.users_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.users_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.users_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.users_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.users_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.users_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.users_table.setObjectName(u"users_table")
        self.users_table.setColumnCount(5)

        self.verticalLayout_2.addWidget(self.users_table)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_delete_user = QPushButton(self.tab_users)
        self.btn_delete_user.setObjectName(u"btn_delete_user")

        self.horizontalLayout.addWidget(self.btn_delete_user)

        self.horizontalSpacer = QSpacerItem(228, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab_users, "")
        self.tab_jobs = QWidget()
        self.tab_jobs.setObjectName(u"tab_jobs")
        self.verticalLayout_3 = QVBoxLayout(self.tab_jobs)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.jobs_table = QTableWidget(self.tab_jobs)
        if (self.jobs_table.columnCount() < 6):
            self.jobs_table.setColumnCount(6)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.jobs_table.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.jobs_table.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.jobs_table.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.jobs_table.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.jobs_table.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.jobs_table.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        self.jobs_table.setObjectName(u"jobs_table")

        self.verticalLayout_3.addWidget(self.jobs_table)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_delete_job = QPushButton(self.tab_jobs)
        self.btn_delete_job.setObjectName(u"btn_delete_job")

        self.horizontalLayout_2.addWidget(self.btn_delete_job)

        self.horizontalSpacer_2 = QSpacerItem(278, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab_jobs, "")
        self.tab_reports = QWidget()
        self.tab_reports.setObjectName(u"tab_reports")
        self.verticalLayout_4 = QVBoxLayout(self.tab_reports)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_refresh_report = QPushButton(self.tab_reports)
        self.btn_refresh_report.setObjectName(u"btn_refresh_report")

        self.verticalLayout_4.addWidget(self.btn_refresh_report)

        self.report_container = QVBoxLayout()
        self.report_container.setObjectName(u"report_container")

        self.verticalLayout_4.addLayout(self.report_container)

        self.tabWidget.addTab(self.tab_reports, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_header.setText(QCoreApplication.translate("Form", u"Admin Paneli", None))
        ___qtablewidgetitem = self.users_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None))
        ___qtablewidgetitem1 = self.users_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Yeni S\u00fctun", None))
        ___qtablewidgetitem2 = self.users_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"E-posta", None))
        ___qtablewidgetitem3 = self.users_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Rol", None))
        ___qtablewidgetitem4 = self.users_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Kay\u0131t Tarihi", None))
        self.btn_delete_user.setText(QCoreApplication.translate("Form", u"Se\u00e7ili Kullan\u0131c\u0131y\u0131 Sil", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_users), QCoreApplication.translate("Form", u"Kullan\u0131c\u0131lar", None))
        ___qtablewidgetitem5 = self.jobs_table.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Yeni S\u00fctun", None))
        ___qtablewidgetitem6 = self.jobs_table.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Ba\u015fl\u0131k", None))
        ___qtablewidgetitem7 = self.jobs_table.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"\u015eirket", None))
        ___qtablewidgetitem8 = self.jobs_table.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Konum", None))
        ___qtablewidgetitem9 = self.jobs_table.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Durum", None))
        ___qtablewidgetitem10 = self.jobs_table.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"Tarih", None))
        self.btn_delete_job.setText(QCoreApplication.translate("Form", u"Se\u00e7ili \u0130lan\u0131 Sil", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_jobs), QCoreApplication.translate("Form", u"T\u00fcm ilanlar", None))
        self.btn_refresh_report.setText(QCoreApplication.translate("Form", u"Yenile", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_reports), QCoreApplication.translate("Form", u"Raporlar", None))
    # retranslateUi

