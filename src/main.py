import sys

from PyQt5.QtWidgets import *

import data
import views


if __name__ == '__main__':
    app = QApplication([])
    window = views.Note('note.txt')
    window.show()
    sys.exit(app.exec_())
