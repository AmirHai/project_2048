import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QTimer
from PyQt5 import uic

RADIUS_OFF_WIDGETS = 5


class MainMenuInit(QWidget):
    def __init__(self):
        super().__init__()
        self.animate_widget = None
        self.GetAllWidgets()

    def GetAllWidgets(self):
        uic.loadUi('../AllActivities/MainMenu.ui', self)
        self.setWindowTitle('2048 - главное окно')
        self.setFixedWidth(600)
        self.setFixedHeight(800)
        # все виджеты в окне, чисто чтобы не путать
        # self.btn_Play; self.btn_Settings; self.btn_Profile;

        self.btn_Play.clicked.connect(self.AnimationOn)
        self.btn_Settings.clicked.connect(self.AnimationOn)
        self.btn_Profile.clicked.connect(self.AnimationOn)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = MainMenuInit()
    game.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
