# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'navegadortnhJPX.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(515, 545)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.navegador_web = QWebEngineView(self.frame)
        self.navegador_web.setObjectName(u"navegador_web")
        self.navegador_web.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_2.addWidget(self.navegador_web)

        self.frame_formato = QFrame(self.frame)
        self.frame_formato.setObjectName(u"frame_formato")
        self.frame_formato.setFrameShape(QFrame.StyledPanel)
        self.frame_formato.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_formato)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_bold = QPushButton(self.frame_formato)
        self.pushButton_bold.setObjectName(u"pushButton_bold")

        self.horizontalLayout.addWidget(self.pushButton_bold)

        self.pushButton_italic = QPushButton(self.frame_formato)
        self.pushButton_italic.setObjectName(u"pushButton_italic")

        self.horizontalLayout.addWidget(self.pushButton_italic)

        self.pushButton_under = QPushButton(self.frame_formato)
        self.pushButton_under.setObjectName(u"pushButton_under")

        self.horizontalLayout.addWidget(self.pushButton_under)

        self.pushButton_color = QPushButton(self.frame_formato)
        self.pushButton_color.setObjectName(u"pushButton_color")

        self.horizontalLayout.addWidget(self.pushButton_color)


        self.verticalLayout_2.addWidget(self.frame_formato)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_2.addWidget(self.textEdit)

        self.pushButton_instertar = QPushButton(self.frame_2)
        self.pushButton_instertar.setObjectName(u"pushButton_instertar")

        self.horizontalLayout_2.addWidget(self.pushButton_instertar)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_bold.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.pushButton_italic.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.pushButton_under.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.pushButton_color.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButton_instertar.setText(QCoreApplication.translate("MainWindow", u"Insertar", None))
    # retranslateUi

