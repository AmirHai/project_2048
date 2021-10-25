import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic


class GameVariates(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('../AllActivities/GameVariates.ui', self)
        self.SetAllSettings()
        self.animate_widget = None

    def SetAllSettings(self):
        self.setWindowTitle('2048 - Запуск Игры')
        self.setFixedHeight(800)
        self.setFixedWidth(600)

        self.btn_back.setIcon(QIcon('../AllPictures/GoBack.png'))
        self.btn_back.setIconSize(QSize(70, 70))
        self.btn_back.clicked.connect(self.ButtonBackOn)
        self.btn_back.clicked.connect(self.GoBackPress)

    def ButtonBackOn(self):
        self.animate_widget = self.sender()
        self.animate_widget.setIcon(QIcon('../AllPictures/GoBackPressed.png'))
        QTimer.singleShot(100, self.ButtonBackOff)

    def ButtonBackOff(self):
        self.animate_widget.setIcon(QIcon('../AllPictures/GoBack.png'))
        self.animate_widget = None

    def GoBackPress(self):
        pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
