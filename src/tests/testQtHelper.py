import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from QtHelper import Data, View, createApp


Count = Data.builder({
    'name': 'bananalone',
    'count': 0,
})


class MainWindow(QWidget, View):
    def __init__(self):
        super().__init__()
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.addBtn = QPushButton('add')
        self.addBtn.clicked.connect(self.add)
        self.resetBtn = QPushButton('reset')
        self.resetBtn.clicked.connect(self.reset)
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        hbox = QHBoxLayout()
        hbox.addWidget(self.addBtn)
        hbox.addWidget(self.resetBtn)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.resize(320, 240)

    def display(self):
        self.label.setText(f'click {self.data["name"]} {self.data["count"]} !')

    def add(self):
        self.data['count'] += 1

    def reset(self):
        self.data.update({'count': 0})


if __name__ == '__main__':
    app = QApplication([])
    # data
    d1 = Count(name='apple')
    d2 = Count()
    # view
    window1 = MainWindow()
    window2 = MainWindow()
    # connect
    createApp(d1).mount(window1)
    createApp(d2).mount(window2)
    # show
    window1.show()
    window2.show()
    sys.exit(app.exec_())
