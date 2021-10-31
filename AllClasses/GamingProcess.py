import sys
import random
import time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5 import uic

COLORS_IN_BLOCKS = ['eee4da', 'ede0c8', 'f2b179', 'f59563',
                    'f67c5f', 'f65e3b', 'edcf72', 'edcc61',
                    'edc850', 'edc53f', 'edc22e']
COLORS_OF_TEXT = ['776e65', 'f9f6f2']


# нахождение степени двойки для установки цвета
def sqrOfTwo(two):
    k = 0
    tw = int(two)
    while tw > 1:
        k += 1
        tw = tw // 2
    return k


def TextColorChoose(two):
    tw = int(two)
    if tw > 4:
        return 1
    else:
        return 0


def AddNewNumber(allNumbs):
    AllClosed = True
    Opened = []
    for i in range(len(allNumbs)):
        for j in range(len(allNumbs[i])):
            if allNumbs[i][j] == ' ':
                AllClosed = False
                Opened.append((i, j))
    if not AllClosed:
        num = random.randint(1, 10)
        if num == 4:
            numb = '4'
        else:
            numb = '2'
        koords = random.choice(Opened)
        allNumbs[koords[0]][koords[1]] = numb


class GameProcess(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('../AllActivities/Game.ui', self)
        self.Points = 0
        self.createWindow()

    def createWindow(self):
        self.setWindowTitle('2048 - Игра')
        self.setFixedHeight(800)
        self.setFixedWidth(600)

        self.koords = [random.randint(0, 3) for _ in range(2)]

        self.btn_restartgame.setIcon(QIcon('../AllPictures/return_in_game.png'))
        self.btn_restartgame.setIconSize(QSize(70, 70))
        self.btn_restartgame.clicked.connect(self.returnGame)

        self.btn_moveback.setIcon(QIcon('../AllPictures/moveBack.png'))
        self.btn_moveback.setIconSize(QSize(70, 70))
        self.btn_moveback.clicked.connect(self.MovingBackEvent)

        self.all_blocks = []
        self.moved_blocks = []
        self.all_buttons = []

        for i in range(4):
            self.all_blocks.append([])
            for j in range(4):
                self.all_blocks[i].append(' ')

        # при вызове функции у нас появляется новое число, которое автоматически записывается
        # при этом он создает сразу два числа
        for _ in range(2):
            AddNewNumber(self.all_blocks)

        for i in range(4):
            self.moved_blocks.append([])
            for j in range(4):
                self.moved_blocks[i].append(self.all_blocks[i][j])

        self.ShowField()

    # пересоздает поле. убирает данные о прошлом поле и показывает новое
    def returnGame(self):
        self.btn_restartgame.setIcon(QIcon('../AllPictures/return_in_game_pressed.png'))
        time.sleep(0.05)
        self.btn_restartgame.setIcon(QIcon('../AllPictures/return_in_game.png'))
        self.all_blocks.clear()
        for i in range(4):
            self.all_blocks.append([])
            for j in range(4):
                self.all_blocks[i].append(' ')
        for _ in range(2):
            AddNewNumber(self.all_blocks)
        self.Points = 0
        self.lcdn_now_points.display(self.Points)
        self.lbl_endgame.setText('')
        self.btn_restartgame.setIcon(QIcon('../AllPictures/return_in_game.png'))
        self.btn_restartgame.setIconSize(QSize(70, 70))
        self.ShowField()

    def MovingBackEvent(self):
        self.all_blocks.clear()
        for i in range(4):
            self.all_blocks.append([])
            for j in range(4):
                self.all_blocks[i].append(self.moved_blocks[i][j])
        self.ShowField()
        self.lbl_endgame.setText('')
        self.btn_restartgame.setIcon(QIcon('../AllPictures/return_in_game.png'))
        self.btn_restartgame.setIconSize(QSize(70, 70))

    # это показывание нашего поля со всеми значениями, записанную специально в отдельную функцию
    def ShowField(self):
        for i in range(4):
            if len(self.all_buttons) < 4:
                self.all_buttons.append([])
            for j in range(4):
                if len(self.all_buttons[i]) < 4:
                    self.all_buttons[i].append(QPushButton(self.frame_with_buts))
                self.pointSize = 25
                self.fontD = self.font()
                self.fontD.setPointSize(self.pointSize)
                self.all_buttons[i][j].setFont(self.fontD)
                self.all_buttons[i][j].setText(self.all_blocks[i][j])
                self.all_buttons[i][j].resize(125, 125)
                self.all_buttons[i][j].move(135 * i + 10, 135 * j + 10)

                if self.all_blocks[i][j] == ' ':
                    self.all_buttons[i][j].setStyleSheet(f'''background-color: rgb(200, 200, 200);
                    border-radius: 15px;
                    ''')
                else:
                    self.all_buttons[i][j].setStyleSheet(
                        f'''background-color: #{COLORS_IN_BLOCKS[sqrOfTwo(self.all_blocks[i][j]) - 1]};
                                        color: #{COLORS_OF_TEXT[TextColorChoose(self.all_blocks[i][j])]};
                                        border-radius: 15px;
                                        ''')
        self.show()

    # пока что тут очень много багов, из-за чего программа плохо работает.
    # возможно у меня получится исправить их к след понедельнику
    def keyPressEvent(self, event):
        if event.nativeVirtualKey() == Qt.Key_W:
            self.clickedEvent('w')
        if event.nativeVirtualKey() == Qt.Key_S:
            self.clickedEvent('s')
        if event.nativeVirtualKey() == Qt.Key_A:
            self.clickedEvent('a')
        if event.nativeVirtualKey() == Qt.Key_D:
            self.clickedEvent('d')

    # это у нас обработчик кнопок клавиатуры, который был описан одно фунцией
    # все переменные, созданные в начале должны инициализироваться от
    def clickedEvent(self, press_btn):
        catchDifferents = False
        startI = (0, 0)
        startJ = (0, 0)
        endI = (0, 0)
        endJ = (0, 0)
        goingI = (0, 0)
        goingJ = (0, 0)
        retI = (0, 0)
        retJ = (0, 0)
        # эти итераторы создают разные значения переменных. так что это не копипаст.
        if press_btn == 'w':
            startI = (-4, -4)
            startJ = (-1, -4)
            endI = (4, 4)
            endJ = (0, 3)
            goingI = (1, 1)
            goingJ = (-1, 1)
            retI = (0, 0)
            retJ = (-1, 1)
        elif press_btn == 's':
            startI = (-4, -4)
            startJ = (-4, -1)
            endI = (4, 4)
            endJ = (3, 0)
            goingI = (1, 1)
            goingJ = (1, -1)
            retI = (0, 0)
            retJ = (1, -1)
        elif press_btn == 'a':
            startI = (-1, -4)
            startJ = (-4, -4)
            endI = (0, 3)
            endJ = (4, 4)
            goingI = (-1, 1)
            goingJ = (1, 1)
            retI = (-1, 1)
            retJ = (0, 0)
        elif press_btn == 'd':
            startI = (-4, -1)
            startJ = (-4, -4)
            endI = (3, 0)
            endJ = (4, 4)
            goingI = (1, -1)
            goingJ = (1, 1)
            retI = (1, -1)
            retJ = (0, 0)
        self.EndGamingEvent()
        for _ in range(4):
            for i in range(4 + startI[0], endI[0], goingI[0]):
                for j in range(4 + startJ[0], endJ[0], goingJ[0]):
                    if self.all_blocks[i + retI[0]][j + retJ[0]] == ' ' and self.all_blocks[i][j] != ' ':
                        self.all_blocks[i + retI[0]][j + retJ[0]] = self.all_blocks[i][j]
                        self.all_blocks[i][j] = ' '
                        catchDifferents = True

        for i in range(4 + startI[1], endI[1], goingI[1]):
            for j in range(4 + startJ[1], endJ[1], goingJ[1]):
                if self.all_blocks[i + retI[1]][j + retJ[1]] == self.all_blocks[i][j] and self.all_blocks[i][j] != ' ':
                    self.all_blocks[i + retI[1]][j + retJ[1]] = str(
                        int(self.all_blocks[i + retI[1]][j + retJ[1]]) + int(self.all_blocks[i][j]))
                    self.all_blocks[i][j] = ' '
                    self.Points += int(self.all_blocks[i + retI[1]][j + retJ[1]])
                    catchDifferents = True

        for _ in range(4):
            for i in range(4 + startI[0], endI[0], goingI[0]):
                for j in range(4 + startJ[0], endJ[0], goingJ[0]):
                    if self.all_blocks[i + retI[0]][j + retJ[0]] == ' ' and self.all_blocks[i][j] != ' ':
                        self.all_blocks[i + retI[0]][j + retJ[0]] = self.all_blocks[i][j]
                        self.all_blocks[i][j] = ' '
                        catchDifferents = True

        if catchDifferents:
            AddNewNumber(self.all_blocks)
        self.lcdn_now_points.display(self.Points)
        self.ShowField()



    def EndGamingEvent(self):
        AllClosed = True
        AllDifferent = True
        for i in range(4):
            for j in range(4):
                if self.all_blocks[i][j] == ' ':
                    AllClosed = False
                if i != 3 and j != 3:
                    if self.all_blocks[i][j] == self.all_blocks[i + 1][j]:
                        AllDifferent = False
                    elif self.all_blocks[i][j + 1] == self.all_blocks[i][j]:
                        AllDifferent = False
                elif i == 3 and j != 3 and self.all_blocks[i][j + 1] == self.all_blocks[i][j]:
                    AllDifferent = False
                elif i != 3 and j == 3 and self.all_blocks[i][j] == self.all_blocks[i + 1][j]:
                    AllDifferent = False
        if AllClosed and AllDifferent:
            self.btn_restartgame.setIcon(QIcon('../AllPictures/endgame_return.png'))
            self.btn_restartgame.setIconSize(QSize(70, 70))
            self.lbl_endgame.setText('Конец игры')
        else:
            self.moved_blocks.clear()
            for i in range(4):
                self.moved_blocks.append([])
                for j in range(4):
                    self.moved_blocks[i].append(self.all_blocks[i][j])



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
