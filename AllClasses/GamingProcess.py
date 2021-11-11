import sys
import random
import time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5 import uic
from AllConstants import *


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
    def __init__(self, x, y, login):
        super().__init__()
        uic.loadUi('../AllActivities/Game.ui', self)
        self.Points = 0
        self.login = login
        self.xSize = x
        self.ySize = y
        self.createWindow()

    def createWindow(self):
        self.setWindowTitle('2048 - Игра')
        self.setFixedWidth(XWINDOWSIZE)
        self.setFixedHeight(YWINDOWSIZE)

        self.size_of_blocks = [(FRAMESIZE - PADDING * (self.xSize + 1)) // self.xSize,
                               (FRAMESIZE - PADDING * (self.ySize + 1)) // self.ySize]

        self.koords = [random.randint(0, self.xSize), random.randint(0, self.ySize)]

        self.btn_restartgame.setIcon(QIcon('../AllPictures/return_in_game.png'))
        self.btn_restartgame.setIconSize(QSize(BUTTONSINGAME, BUTTONSINGAME))
        self.btn_restartgame.clicked.connect(self.returnGame)

        self.btn_moveback.setIcon(QIcon('../AllPictures/moveBack.png'))
        self.btn_moveback.setIconSize(QSize(BUTTONSINGAME, BUTTONSINGAME))
        self.btn_moveback.clicked.connect(self.MovingBackEvent)

        self.records = open(f'../allCSVFiles/records_{self.login}.csv', encoding='utf8').readlines()
        self.rec = self.records[6 * (self.xSize - 3) + self.ySize - 3].split(";")[2]
        self.lcdn_record_points.display(int(self.rec))

        self.all_blocks = []
        self.moved_blocks = []
        self.all_buttons = []

        for i in range(self.xSize):
            self.all_blocks.append([])
            for j in range(self.ySize):
                self.all_blocks[i].append(' ')

        # при вызове функции у нас появляется новое число, которое автоматически записывается
        # при этом он создает сразу два числа
        for _ in range(2):
            AddNewNumber(self.all_blocks)

        for i in range(self.xSize):
            self.moved_blocks.append([])
            for j in range(self.ySize):
                self.moved_blocks[i].append(self.all_blocks[i][j])

        self.ShowField()

    def newRecords(self, newRec):
        allrec = open(f'../allCSVFiles/records_{self.login}.csv', encoding='utf8').readlines()
        recordwriting = open(f'../allCSVFiles/records_{self.login}.csv', 'w', encoding='utf8')
        for i in allrec:
            if i.split(';')[0] == str(self.xSize) and i.split(';')[1] == str(self.ySize):
                recordwriting.write(';'.join([str(self.xSize), str(self.ySize), str(newRec), '\n']))
            else:
                recordwriting.write(i)

    # пересоздает поле. убирает данные о прошлом поле и показывает новое
    def returnGame(self):
        self.btn_restartgame.setIcon(QIcon('../AllPictures/return_in_game_pressed.png'))
        time.sleep(0.05)
        self.btn_restartgame.setIcon(QIcon('../AllPictures/return_in_game.png'))
        self.all_blocks.clear()
        for i in range(self.xSize):
            self.all_blocks.append([])
            for j in range(self.ySize):
                self.all_blocks[i].append(' ')
        for _ in range(2):
            AddNewNumber(self.all_blocks)
        if self.Points > int(self.rec):
            self.newRecords(self.Points)
        self.Points = 0
        self.lcdn_now_points.display(self.Points)
        self.lbl_endgame.setText('')
        self.btn_restartgame.setIcon(QIcon('../AllPictures/return_in_game.png'))
        self.btn_restartgame.setIconSize(QSize(BUTTONSINGAME, BUTTONSINGAME))
        self.ShowField()

    def MovingBackEvent(self):
        self.all_blocks.clear()
        for i in range(self.xSize):
            self.all_blocks.append([])
            for j in range(self.ySize):
                self.all_blocks[i].append(self.moved_blocks[i][j])
        self.ShowField()
        self.lbl_endgame.setText('')
        self.btn_restartgame.setIcon(QIcon('../AllPictures/return_in_game.png'))
        self.btn_restartgame.setIconSize(QSize(BUTTONSINGAME, BUTTONSINGAME))

    # это показывание нашего поля со всеми значениями, записанную специально в отдельную функцию
    def ShowField(self):
        for i in range(self.xSize):
            self.all_buttons.append([])
            for j in range(self.ySize):
                self.all_buttons[i].append(QPushButton(self.frame_with_buts))
                self.pointSize = 25
                self.fontD = self.font()
                self.fontD.setPointSize(self.pointSize)
                self.all_buttons[i][j].setFont(self.fontD)
                self.all_buttons[i][j].setText(self.all_blocks[i][j])
                self.all_buttons[i][j].resize(self.size_of_blocks[0], self.size_of_blocks[1])
                self.all_buttons[i][j].move((self.size_of_blocks[0] + PADDING) * i + PADDING,
                                            (self.size_of_blocks[1] + PADDING) * j + PADDING)

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
        self.records = open(f'../allCSVFiles/records_{self.login}.csv', encoding='utf8').readlines()
        self.rec = self.records[6 * (self.xSize - 3) + self.ySize - 3].split(";")[2]
        self.lcdn_record_points.display(int(self.rec))
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
            startI = (-1 * self.xSize, -1 * self.xSize)
            startJ = (-1, -1 * self.ySize)
            endI = (self.xSize, self.xSize)
            endJ = (0, self.ySize - 1)
            goingI = (1, 1)
            goingJ = (-1, 1)
            retI = (0, 0)
            retJ = (-1, 1)
        elif press_btn == 's':
            startI = (-1 * self.xSize, -1 * self.xSize)
            startJ = (-1 * self.ySize, -1)
            endI = (self.xSize, self.xSize)
            endJ = (self.ySize - 1, 0)
            goingI = (1, 1)
            goingJ = (1, -1)
            retI = (0, 0)
            retJ = (1, -1)
        elif press_btn == 'a':
            startI = (-1, -1 * self.xSize)
            startJ = (-1 * self.ySize, -1 * self.ySize)
            endI = (0, self.xSize - 1)
            endJ = (self.ySize, self.ySize)
            goingI = (-1, 1)
            goingJ = (1, 1)
            retI = (-1, 1)
            retJ = (0, 0)
        elif press_btn == 'd':
            startI = (-1 * self.xSize, -1)
            startJ = (-1 * self.ySize, -1 * self.ySize)
            endI = (self.xSize - 1, 0)
            endJ = (self.ySize, self.ySize)
            goingI = (1, -1)
            goingJ = (1, 1)
            retI = (1, -1)
            retJ = (0, 0)
        self.EndGamingEvent()
        for _ in range(max(self.xSize, self.ySize)):
            for i in range(self.xSize + startI[0], endI[0], goingI[0]):
                for j in range(self.ySize + startJ[0], endJ[0], goingJ[0]):
                    if self.all_blocks[i + retI[0]][j + retJ[0]] == ' ' and self.all_blocks[i][j] != ' ':
                        self.all_blocks[i + retI[0]][j + retJ[0]] = self.all_blocks[i][j]
                        self.all_blocks[i][j] = ' '
                        catchDifferents = True

        for i in range(self.xSize + startI[1], endI[1], goingI[1]):
            for j in range(self.ySize + startJ[1], endJ[1], goingJ[1]):
                if self.all_blocks[i + retI[1]][j + retJ[1]] == self.all_blocks[i][j] and self.all_blocks[i][j] != ' ':
                    self.all_blocks[i + retI[1]][j + retJ[1]] = str(
                        int(self.all_blocks[i + retI[1]][j + retJ[1]]) + int(self.all_blocks[i][j]))
                    self.all_blocks[i][j] = ' '
                    self.Points += int(self.all_blocks[i + retI[1]][j + retJ[1]])
                    catchDifferents = True

        for _ in range(max(self.xSize, self.ySize)):
            for i in range(self.xSize + startI[0], endI[0], goingI[0]):
                for j in range(self.ySize + startJ[0], endJ[0], goingJ[0]):
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
        for i in range(self.xSize):
            for j in range(self.ySize):
                if self.all_blocks[i][j] == ' ':
                    AllClosed = False
                if i != self.xSize - 1 and j != self.ySize - 1:
                    if self.all_blocks[i][j] == self.all_blocks[i + 1][j]:
                        AllDifferent = False
                    elif self.all_blocks[i][j + 1] == self.all_blocks[i][j]:
                        AllDifferent = False
                elif i == self.xSize - 1 and j != self.ySize - 1 and self.all_blocks[i][j + 1] == self.all_blocks[i][
                    j]:
                    AllDifferent = False
                elif i != self.xSize - 1 and j == self.ySize - 1 and self.all_blocks[i][j] == self.all_blocks[i + 1][
                    j]:
                    AllDifferent = False
        if AllClosed and AllDifferent:
            self.btn_restartgame.setIcon(QIcon('../AllPictures/endgame_return.png'))
            self.btn_restartgame.setIconSize(QSize(BUTTONSINGAME, BUTTONSINGAME))
            self.lbl_endgame.setText('Конец игры')
            self.newRecords(self.Points)
        else:
            self.moved_blocks.clear()
            for i in range(self.xSize):
                self.moved_blocks.append([])
                for j in range(self.ySize):
                    self.moved_blocks[i].append(self.all_blocks[i][j])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
