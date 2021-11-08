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
                    recordwriting.write(';'.join([str(i), str(j), '0', '\n']))
        query = f''' SELECT * FROM profiles WHERE login = '{self.login}' '''
        allrec = self.cursor.execute(query).fetchall()
        self.ledit_nickname.setText(allrec[0][2])
        # пока что вашего статуса нету, тк я его еще не добавил в дб
        self.ledit_status.setText(allrec[0][1])




def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
