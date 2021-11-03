import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic
from AllConstants import *


class ProfileClass(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('../AllActivities/Profile.ui', self)
        self.SetAllSettings()

    def SetAllSettings(self):
        self.setWindowTitle('2048 - Профиль игрока')
        self.setFixedWidth(XWINDOWSIZE)
        self.setFixedHeight(YWINDOWSIZE)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)