import ProfileClass
import GameVariates

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from PyQt5 import uic
from AllConstants import *

RADIUS_OFF_WIDGETS = 5


class MainMenuInit(QWidget):
    def __init__(self, login):
        super().__init__()
        self.animate_widget = None
        self.login = login
        self.GetAllWidgets()


    def GetAllWidgets(self):
        uic.loadUi('../AllActivities/MainMenu.ui', self)
        self.setWindowTitle('2048 - главное окно')
        self.setFixedWidth(XWINDOWSIZE)
        self.setFixedHeight(YWINDOWSIZE)
        # все виджеты в окне, чисто чтобы не путать
        # self.btn_Play; self.btn_Settings; self.btn_Profile;

        self.btn_play.clicked.connect(self.AnimationOn)
        self.btn_play.clicked.connect(self.GamesClicked)

        self.btn_settings.clicked.connect(self.AnimationOn)

        self.btn_profile.clicked.connect(self.AnimationOn)
        self.btn_profile.clicked.connect(self.ProfileClicked)

        self.btn_design.clicked.connect(self.AnimationOn)

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

    def ProfileClicked(self):
        self.profile = ProfileClass.ProfileClass(self.login)
        self.profile.show()

    def GamesClicked(self):
        self.games = GameVariates.GameVariates(self.login)
        self.games.show()

    # с будущем все настройки будут добавлены(на самом деле я пока что не придумал что туда добавить)
    def SettingsClicked(self):
        self.settings = None


