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


# получение значения числа
def getNumber():
    num = random.randint(1, 10)
    if num == 4:
        return '4'
    else:
        return '2'


# нахождение степени двойки
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


class GameProcess(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('../AllActivities/Game.ui', self)
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

        # второй цикл нужен для того, чтобы кнопки не оказались в одном месте
        # так я задаю два начальных числа
        while self.all_blocks[self.koords[0]][self.koords[1]] != ' ':
            self.koords = [random.randint(0, 3) for _ in range(2)]
        self.all_blocks[self.koords[0]][self.koords[1]] = getNumber()

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
        print('rrr')

    # пока что тут очень много багов, изза чего программа плохо работает.
    # возможно у меня получится исправить их к след понедельнику
    def keyPressEvent(self, event):
        if event.nativeVirtualKey() == Qt.Key_W:
            self.aClickedEvent()
        if event.nativeVirtualKey() == Qt.Key_S:
            self.sClickedEvent()

    def aClickedEvent(self):
        print(*self.all_blocks)
        for i in range(4):
            for j in range(3, 0, -1):
                if self.all_blocks[i][j - 1] == ' ':
                    self.all_blocks[i][j - 1] = self.all_blocks[i][j]
                    self.all_blocks[i][j] = ' '
        self.ShowField()

    def sClickedEvent(self):
        print(*self.all_blocks)
        for i in range(4):
            for j in range(3):
                if self.all_blocks[i][j + 1] == ' ':
                    self.all_blocks[i][j + 1] = self.all_blocks[i][j]
                    self.all_blocks[i][j] = ' '
        self.ShowField()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
