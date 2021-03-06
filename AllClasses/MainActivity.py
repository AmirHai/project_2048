import sys

from registration import *
from PyQt5.QtWidgets import *


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


# окно регистрации еще чутка глючное, так что я его пропустил
if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = RegistrationClass()
    game.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
