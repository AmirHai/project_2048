import sys

from MainMenuClass import *
from PyQt5.QtWidgets import *


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = MainMenuInit()
    game.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
