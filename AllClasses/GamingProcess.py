import sys
import random

from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
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

        self.all_blocks = []
        self.all_buttons = []

        for i in range(4):
            self.all_blocks.append([])
            for j in range(4):
                self.all_blocks[i].append(' ')

        # при вызове функции у нас появляется новое число, которое автоматически записывается
        # при этом он создает сразу два числа
        for _ in range(2):
            AddNewNumber(self.all_blocks)

        self.ShowField()

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

    # пока что тут очень много багов, изза чего программа плохо работает.
    # возможно у меня получится исправить их к след понедельнику
    def keyPressEvent(self, event):
        if event.nativeVirtualKey() == Qt.Key_W:
            self.wClickedEvent()
        if event.nativeVirtualKey() == Qt.Key_S:
            self.sClickedEvent()
        if event.nativeVirtualKey() == Qt.Key_A:
            self.aClickedEvent()
        if event.nativeVirtualKey() == Qt.Key_D:
            self.dClickedEvent()

    # ВСЕ ФУНКЦИИ ТУТ РАЗНЫЕ И ДЕЛАЮТ РАЗНЫЕ ПРЕОБРАЗОВАНИЯ
    # даже если тут похоже, что многое одинаково, то нет, преобразовать это не получится в единую систему
    def wClickedEvent(self):
        catchDifferents = False
        for _ in range(4):
            for i in range(4):
                for j in range(3, 0, -1):
                    if self.all_blocks[i][j - 1] == ' ' and self.all_blocks[i][j] != ' ':
                        self.all_blocks[i][j - 1] = self.all_blocks[i][j]
                        self.all_blocks[i][j] = ' '
                        catchDifferents = True
        for i in range(4):
            for j in range(3):
                if self.all_blocks[i][j + 1] == self.all_blocks[i][j] and self.all_blocks[i][j] != ' ':
                    self.all_blocks[i][j + 1] = str(int(self.all_blocks[i][j + 1]) + int(self.all_blocks[i][j]))
                    self.all_blocks[i][j] = ' '
                    catchDifferents = True
        for _ in range(4):
            for i in range(4):
                for j in range(3, 0, -1):
                    if self.all_blocks[i][j - 1] == ' ' and self.all_blocks[i][j] != ' ':
                        self.all_blocks[i][j - 1] = self.all_blocks[i][j]
                        self.all_blocks[i][j] = ' '
                        catchDifferents = True
        if catchDifferents:
            AddNewNumber(self.all_blocks)
        self.ShowField()

    def sClickedEvent(self):
        catchDifferents = False
        for _ in range(4):
            for i in range(4):
                for j in range(3):
                    if self.all_blocks[i][j + 1] == ' ' and self.all_blocks[i][j] != ' ':
                        self.all_blocks[i][j + 1] = self.all_blocks[i][j]
                        self.all_blocks[i][j] = ' '
                        catchDifferents = True
        for i in range(4):
            for j in range(3, 0, -1):
                if self.all_blocks[i][j - 1] == self.all_blocks[i][j] and self.all_blocks[i][j] != ' ':
                    self.all_blocks[i][j - 1] = str(int(self.all_blocks[i][j - 1]) + int(self.all_blocks[i][j]))
                    self.all_blocks[i][j] = ' '
                    catchDifferents = True
        for _ in range(4):
            for i in range(4):
                for j in range(3):
                    if self.all_blocks[i][j + 1] == ' ' and self.all_blocks[i][j] != ' ':
                        self.all_blocks[i][j + 1] = self.all_blocks[i][j]
                        self.all_blocks[i][j] = ' '
                        catchDifferents = True
        if catchDifferents:
            AddNewNumber(self.all_blocks)
        self.ShowField()

    def aClickedEvent(self):
        catchDifferents = False
        for _ in range(4):
            for i in range(3, 0, -1):
                for j in range(4):
                    if self.all_blocks[i - 1][j] == ' ' and self.all_blocks[i][j] != ' ':
                        self.all_blocks[i - 1][j] = self.all_blocks[i][j]
                        self.all_blocks[i][j] = ' '
                        catchDifferents = True
        for i in range(3):
            for j in range(4):
                if self.all_blocks[i + 1][j] == self.all_blocks[i][j] and self.all_blocks[i][j] != ' ':
                    self.all_blocks[i + 1][j] = str(int(self.all_blocks[i + 1][j]) + int(self.all_blocks[i][j]))
                    self.all_blocks[i][j] = ' '
                    catchDifferents = True
        for _ in range(4):
            for i in range(3, 0, -1):
                for j in range(4):
                    if self.all_blocks[i - 1][j] == ' ' and self.all_blocks[i][j] != ' ':
                        self.all_blocks[i - 1][j] = self.all_blocks[i][j]
                        self.all_blocks[i][j] = ' '
                        catchDifferents = True
        if catchDifferents:
            AddNewNumber(self.all_blocks)
        self.ShowField()

    def dClickedEvent(self):
        catchDifferents = False
        for _ in range(4):
            for i in range(3):
                for j in range(4):
                    if self.all_blocks[i + 1][j] == ' ' and self.all_blocks[i][j] != ' ':
                        self.all_blocks[i + 1][j] = self.all_blocks[i][j]
                        self.all_blocks[i][j] = ' '
                        catchDifferents = True
        for i in range(3, 0, -1):
            for j in range(4):
                if self.all_blocks[i - 1][j] == self.all_blocks[i][j] and self.all_blocks[i][j] != ' ':
                    self.all_blocks[i - 1][j] = str(int(self.all_blocks[i - 1][j]) + int(self.all_blocks[i][j]))
                    self.all_blocks[i][j] = ' '
                    catchDifferents = True
        for _ in range(4):
            for i in range(3):
                for j in range(4):
                    if self.all_blocks[i + 1][j] == ' ' and self.all_blocks[i][j] != ' ':
                        self.all_blocks[i + 1][j] = self.all_blocks[i][j]
                        self.all_blocks[i][j] = ' '
                        catchDifferents = True
        if catchDifferents:
            AddNewNumber(self.all_blocks)
        self.ShowField()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
