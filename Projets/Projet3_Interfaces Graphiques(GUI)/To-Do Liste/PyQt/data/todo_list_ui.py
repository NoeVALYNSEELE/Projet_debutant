# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'todo_list.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(340, 282)
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 331, 251))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.task_list = QListWidget(self.formLayoutWidget)
        self.task_list.setObjectName(u"task_list")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.task_list)

        self.input_task = QLineEdit(self.formLayoutWidget)
        self.input_task.setObjectName(u"input_task")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.input_task)

        self.button_done = QPushButton(self.formLayoutWidget)
        self.button_done.setObjectName(u"button_done")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.button_done)

        self.button_add = QPushButton(self.formLayoutWidget)
        self.button_add.setObjectName(u"button_add")
        self.button_add.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.button_add)

        self.button_delete = QPushButton(self.formLayoutWidget)
        self.button_delete.setObjectName(u"button_delete")
        self.button_delete.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.button_delete)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 340, 18))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_done.setText(QCoreApplication.translate("MainWindow", u"Terminer", None))
        self.button_add.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.button_delete.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
    # retranslateUi

