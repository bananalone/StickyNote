from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from QtHelper import View


class TextEdit(QWidget, View):
    def __init__(self, text: str = ''):
        super().__init__()
        self._textEdit = QTextEdit()
        self._textEdit.setStyleSheet('border-bottom-right-radius: 15px')
        self._textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self._textEdit.setPlainText(text)
        self._textEdit.textChanged.connect(self._textChanged)
        hbox = QHBoxLayout()
        hbox.addWidget(self._textEdit)
        hbox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(hbox)

    def display(self):
        print(f'TextEdit: {self.data}')
        self._textEdit.setFont(QFont('宋体', self.data['fontSize']))
        backgroundColor = self.getBackgroundColor()
        if backgroundColor:
            self.setStyleSheet(f'background-color: {backgroundColor}')

    def getBackgroundColor(self) -> str | None:
        if self.data['backgroundColor'] == 'green':
            return '#C7EDCC'
        else:
            return None

    def _textChanged(self):
        self.data['text'] = self._textEdit.toPlainText()
