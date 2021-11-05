import MainMenuClass
import sqlite3

from PyQt5.QtWidgets import *
from PyQt5 import uic
from AllConstants import *


class RegistrationClass(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('../AllActivities/registrationActivity.ui', self)
        self.setFixedWidth(XREGISTRSIZE)
        self.setFixedHeight(YREGISTRSIZE)

        self.db = sqlite3.connect('profiles_db.db')

        self.btn_registr.clicked.connect(self.Registrate)
        self.btn_avtoriz.clicked.connect(self.LoginToGame)

    def Registrate(self):
        self.lbl_error_value.setText('')
        cursor = self.db.cursor()
        if self.ledit_login.text() != '' and len(self.ledit_password.text()) >= 8:
            query = f''' INSERT INTO profiles (login, password) VALUES({self.ledit_login.text()}, {self.ledit_password.text()}) '''
            cursor.execute(query)
            self.db.commit()
            self.db.close()
            self.menu = MainMenuClass.MainMenuInit()
            self.close()
        else:
            self.lbl_error_value.setText('Некоррекные данные')

    def LoginToGame(self):
        self.lbl_error_value.setText('')
        cursor = self.db.cursor()
        query = f''' SELECT * FROM profiles WHERE login = {self.ledit_login.text()}'''
        resourses = cursor.execute(query).fetchall()
        for i in resourses:
            if i[1] == self.ledit_password.text():
                self.db.close()
                self.menu = MainMenuClass.MainMenuInit()
                self.close()
        self.lbl_error_value.setText('неверный логин или пароль')
