import sys
import GamingProcess

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from AllConstants import *


class GameVariates(QWidget):
    def __init__(self, login):
        super().__init__()
        self.login = login
        uic.loadUi('../AllActivities/GameVariates.ui', self)
        self.SetAllSettings()
        self.x_Size = XFRAMESIZE
        self.y_Size = YFRAMESIZE
        self.animate_widget = None

    def SetAllSettings(self):
        self.setWindowTitle('2048 - Запуск Игры')
        self.setFixedWidth(XWINDOWSIZE)
        self.setFixedHeight(YWINDOWSIZE)


        self.btn_back.setIcon(QIcon('../AllPictures/GoBack.png'))
        self.btn_back.setIconSize(QSize(BUTTONSINGAME, BUTTONSINGAME))
        self.btn_back.clicked.connect(self.GoBackPress)

        self.btn_play_game.clicked.connect(self.StartGaming)

        self.X_size_of_frame.valueChanged.connect(self.XSliderMoved)
        self.Y_size_of_frame.valueChanged.connect(self.YSliderMoved)

    def XSliderMoved(self):
        self.x_Size = self.X_size_of_frame.value()

    def YSliderMoved(self):
        self.y_Size = self.Y_size_of_frame.value()

    def GoBackPress(self):
        pass

    def StartGaming(self):
        self.gaming = GamingProcess.GameProcess(self.x_Size, self.y_Size, self.login)
        self.gaming.show()
        self.hide()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
