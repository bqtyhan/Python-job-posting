# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'job_card.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_JobCard(object):
    def setupUi(self, JobCard):
        if not JobCard.objectName():
            JobCard.setObjectName(u"JobCard")
        JobCard.resize(400, 120)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(JobCard.sizePolicy().hasHeightForWidth())
        JobCard.setSizePolicy(sizePolicy)
        JobCard.setMinimumSize(QSize(0, 110))
        JobCard.setMaximumSize(QSize(16777215, 120))
        self.verticalLayout_3 = QVBoxLayout(JobCard)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(JobCard)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"#JobCard { \n"
"    background-color: white;\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#JobCard:hover {\n"
"    border-color: #2563eb;\n"
"}\n"
"\n"
"/* \u015eirket, Konum ve Maa\u015f etiketleri i\u00e7in modern kaps\u00fcl stili */\n"
"#lbl_company, #lbl_location, #lbl_salary {\n"
"    background-color: #f8fafc; /* \u00c7ok a\u00e7\u0131k gri arka plan */\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 12px;\n"
"    padding: 4px 12px;\n"
"    color: #475569;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"/* Etiketlerin \u00fczerine gelince renk de\u011fi\u015fimi */\n"
"#lbl_company:hover, #lbl_location:hover, #lbl_salary:hover {\n"
"    background-color: #e2e8f0;\n"
"    color: #1e293b;\n"
"}\n"
"\n"
"#lbl_title {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: #1e293b;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_title = QLabel(self.frame)
        self.lbl_title.setObjectName(u"lbl_title")

        self.horizontalLayout.addWidget(self.lbl_title)

        self.lbl_date = QLabel(self.frame)
        self.lbl_date.setObjectName(u"lbl_date")

        self.horizontalLayout.addWidget(self.lbl_date)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lbl_company = QLabel(self.frame)
        self.lbl_company.setObjectName(u"lbl_company")

        self.verticalLayout.addWidget(self.lbl_company)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbl_location = QLabel(self.frame)
        self.lbl_location.setObjectName(u"lbl_location")

        self.horizontalLayout_2.addWidget(self.lbl_location)

        self.lbl_salary = QLabel(self.frame)
        self.lbl_salary.setObjectName(u"lbl_salary")

        self.horizontalLayout_2.addWidget(self.lbl_salary)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.frame)


        self.retranslateUi(JobCard)

        QMetaObject.connectSlotsByName(JobCard)
    # setupUi

    def retranslateUi(self, JobCard):
        JobCard.setWindowTitle(QCoreApplication.translate("JobCard", u"Form", None))
#if QT_CONFIG(tooltip)
        self.lbl_title.setToolTip(QCoreApplication.translate("JobCard", u"\u0130\u015f Ad\u0131", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_title.setText(QCoreApplication.translate("JobCard", u"TextLabel", None))
#if QT_CONFIG(tooltip)
        self.lbl_date.setToolTip(QCoreApplication.translate("JobCard", u"Tarih", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_date.setText(QCoreApplication.translate("JobCard", u"TextLabel", None))
#if QT_CONFIG(tooltip)
        self.lbl_company.setToolTip(QCoreApplication.translate("JobCard", u"\u0130\u015f Veren \u015eirket", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_company.setText(QCoreApplication.translate("JobCard", u"TextLabel", None))
#if QT_CONFIG(tooltip)
        self.lbl_location.setToolTip(QCoreApplication.translate("JobCard", u"Konum", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_location.setText(QCoreApplication.translate("JobCard", u"TextLabel", None))
        self.lbl_salary.setText(QCoreApplication.translate("JobCard", u"TextLabel", None))
    # retranslateUi

