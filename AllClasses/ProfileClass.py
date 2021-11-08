import sys
import sqlite3

from PyQt5.QtWidgets import *
from PyQt5 import uic
from AllConstants import *


class ProfileClass(QWidget):
    def __init__(self, login):
        super().__init__()
        self.login = login
        uic.loadUi('../AllActivities/Profile.ui', self)
        self.SetAllSettings()

    def SetAllSettings(self):
        self.setWindowTitle('2048 - Профиль игрока')
        self.setFixedWidth(XWINDOWSIZE)
        self.setFixedHeight(YWINDOWSIZE)

        self.db = sqlite3.connect('profiles_db.db')
        self.cursor = self.db.cursor()

        recordwriting = open(f'records_{self.login}.csv', 'w', encoding='utf8')
        records = open(f'records_{self.login}.csv', encoding='utf8')
        # числа 3 и 9 появились из-за того, что это минимальные и максимальные значения размера поля
        # в игре. а все записанные нули это сами рекорды
        if len(records.readlines()) == 0:
            for i in range(3, 9):
                for j in range(3, 9):
                    recordwriting.write(';'.join([str(i), str(j), '0']))
        layout = QGridLayout()
        for i in records.readlines():
            rec = QLabel(i)
            layout.addWidget(rec)
        w = QWidget()
        w.setLayout(layout)
        self.scrollArea_records.setWidget(w)



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
