import sys

from PyQt5.QtWidgets import QWidget
from PyQt5 import uic


class ProfileClass(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('../AllActivities/Profile.ui', self)
        self.SetAllSettings()

    def SetAllSettings(self):
        self.setWindowTitle('Профиль игрока - 2048')
        self.setFixedHeight(800)
        self.setFixedWidth(600)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)