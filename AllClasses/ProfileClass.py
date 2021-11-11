import sys
import sqlite3

from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QTimer
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

        self.records = open(f'../allCSVFiles/records_{self.login}.csv', encoding='utf8').readlines()
        # числа 3 и 9 появились из-за того, что это минимальные и максимальные значения размера поля
        # в игре. а все записанные нули это сами рекорды
        for i in range(3, 9):
            for j in range(3, 9):
                but = QPushButton(self.btns_allRecords)
                but.move(90 * (i - 3), 90 * (j - 3))
                but.resize(80, 80)
                but.setText(f'{i}x{j}')
                but.setStyleSheet('''background-color: rgb(255, 174, 0, 240);
                                                            border-radius: 15px;
                                                            border-color: black;
                                                            border-style: outset;
                                                            border-width: 2px;
                                                            border-radius: 15px;''')
                but.clicked.connect(self.AnimationOn)
                but.clicked.connect(self.recordOpened)
        query = f''' SELECT * FROM profiles WHERE login = '{self.login}' '''
        allrec = self.cursor.execute(query).fetchall()
        self.ledit_nickname.setText(allrec[0][2])
        # пока что вашего статуса нету, тк я его еще не добавил в дб
        self.ledit_status.setText(allrec[0][1])

    def recordOpened(self):
        with open(f'../allCSVFiles/records_{self.login}.csv', encoding='utf8') as record:
            i = int(self.sender().text()[0])
            j = int(self.sender().text()[2])
            self.mass = record.readlines()
            self.lbl_record.setText(f'{i} x {j}: {self.mass[6 * (i - 3) + j - 3].split(";")[2]}')

    def AnimationOn(self):
        # анимация кнопки при нажатии
        # при слишком быстром нажатии вылезает ошибка, которая никак не влияет на приложение
        self.animate_widget = self.sender()
        self.animate_widget.setStyleSheet('''background-color: rgb(255, 150, 0, 240);
                                            border-radius: 15px;
                                            border-color: black;
                                            border-style: outset;
                                            border-width: 2px;
                                            border-radius: 15px;''')
        QTimer.singleShot(100, self.AnimationOff)

    def AnimationOff(self):
        self.animate_widget.setStyleSheet('''background-color: rgb(255, 174, 0, 240);
                                            border-radius: 15px;
                                            border-color: black;
                                            border-style: outset;
                                            border-width: 2px;
                                            border-radius: 15px;''')
        self.animate_widget = None


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

