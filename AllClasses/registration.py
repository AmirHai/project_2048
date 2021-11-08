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
        self.setWindowTitle('Авторизация')

        self.db = sqlite3.connect('profiles_db.db')

        self.btn_registr.clicked.connect(self.Registrate)
        self.btn_avtoriz.clicked.connect(self.LoginToGame)

        self.db = sqlite3.connect('profiles_db.db')
        self.cursor = self.db.cursor()

    def Registrate(self):
        Opened = True
        self.lbl_error_value.setText('')
        allLogins = self.cursor.execute(f''' SELECT login FROM allLogins WHERE login = '{self.ledit_login.text()}' ''').fetchall()
        if len(allLogins) != 0:
            Opened = False
        if self.ledit_login.text() != '' and len(self.ledit_password.text()) >= 8 and Opened:
            query = f''' INSERT INTO allLogins (login, password) VALUES('{self.ledit_login.text()}', '{self.ledit_password.text()}') '''
            self.cursor.execute(query)
            self.db.commit()
            self.menu = MainMenuClass.MainMenuInit(self.ledit_login.text())
            self.menu.show()
            self.hide()
        elif not Opened:
            errorWindow = QMessageBox()
            errorWindow.setIcon(QMessageBox.Critical)
            errorWindow.setWindowTitle("ошибка регистрации")
            errorWindow.setText('данный логин уже занят')
            errorWindow.exec_()
        else:
            errorWindow = QMessageBox()
            errorWindow.setIcon(QMessageBox.Critical)
            errorWindow.setWindowTitle("ошибка регистрации")
            errorWindow.setText('некорректный логин или пароль')
            errorWindow.exec_()
        query = f''' INSERT INTO profiles (login, status, nickname, bestRecord)
         VALUES('{self.ledit_login.text()}', 'Нет', '{self.ledit_login.text()}', 0) '''
        self.cursor.execute(query)
        self.db.commit()

    def LoginToGame(self):
        self.lbl_error_value.setText('')
        query = f''' SELECT * FROM allLogins WHERE login = '{self.ledit_login.text()}' '''
        resourses = self.cursor.execute(query).fetchall()
        windowOpened = True
        for i in resourses:
            if i[1] == self.ledit_password.text():
                self.db.close()
                self.menu = MainMenuClass.MainMenuInit(self.ledit_login.text())
                self.menu.show()
                self.hide()
                windowOpened = False
        if windowOpened:
            errorWindow = QMessageBox()
            errorWindow.setIcon(QMessageBox.Critical)
            errorWindow.setWindowTitle("ошибка входа")
            errorWindow.setText('неверный логин или пароль')
            errorWindow.exec_()
