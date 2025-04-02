# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Test-pyqt-designer.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(491, 227)
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(16)
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Bouton_montrer = QPushButton(self.centralwidget)
        self.Bouton_montrer.setObjectName(u"Bouton_montrer")
        self.Bouton_montrer.setGeometry(QRect(110, 70, 91, 31))
        self.Bouton_cacher = QPushButton(self.centralwidget)
        self.Bouton_cacher.setObjectName(u"Bouton_cacher")
        self.Bouton_cacher.setGeometry(QRect(240, 70, 91, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 130, 191, 31))
        font1 = QFont()
        font1.setFamilies([u"Kunstler Script"])
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setUnderline(True)
        self.label.setFont(font1)
        self.label.setAutoFillBackground(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.image_label = QLabel(self.centralwidget)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setGeometry(QRect(350, 120, 111, 61))
        self.image_label.setMouseTracking(False)
        self.image_label.setPixmap(QPixmap(u"../../Images/Saved Pictures/ca_marche.png"))
        self.image_label.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Bouton_montrer.clicked.connect(self.label.show)
        self.Bouton_cacher.clicked.connect(self.label.hide)
        self.Bouton_montrer.clicked.connect(self.image_label.show)
        self.Bouton_cacher.clicked.connect(self.image_label.hide)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Bouton_montrer.setText(QCoreApplication.translate("MainWindow", u"Montrer", None))
        self.Bouton_cacher.setText(QCoreApplication.translate("MainWindow", u"Cacher", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"No\u00e9 VALYNSEELE", None))
        self.image_label.setText("")
    # retranslateUi

