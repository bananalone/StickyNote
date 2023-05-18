from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from QtHelper import View


class MenuBar(QWidget, View):
    def __init__(self):
        super().__init__()
        btnSize = QSize(40, 40)
        self._titleLabel = QLabel('StickNote')
        self._titleLabel.setFont(QFont('Times New Roman', 10))
        self._closeBtn = QPushButton('×')
        self._closeBtn.setFixedSize(btnSize)
        self._closeBtn.clicked.connect(self._quit)
        self._minimizeBtn = QPushButton('-')
        self._minimizeBtn.setFixedSize(btnSize)
        self._minimizeBtn.clicked.connect(self._showMinimized)
        hbox = QHBoxLayout()
        hbox.addWidget(self._titleLabel)
        hbox.addWidget(self._minimizeBtn)
        hbox.addWidget(self._closeBtn)
        hbox.setSpacing(0)
        hbox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(hbox)
        self._titleLabel.setStyleSheet('border-top-left-radius:15px')
        self._mousePressed = False
        self._startPos = None

    def display(self):
        backgroundColor = self.getBackgroundColor()
        if backgroundColor:
            self.setStyleSheet(f'background-color: {backgroundColor}')

    def getBackgroundColor(self) -> str | None:
        if self.data['backgroundColor'] == 'green':
            return '#B7E8BD'
        else:
            return None

    def _quit(self):
        self.data['close'] = True

    def _showMinimized(self):
        self.data['showMinimized'] = True

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self._mousePressed = True
            self.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))  # 更改鼠标图标
            self._startPos = event.globalPos()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self._mousePressed:
            pos = event.globalPos()
            relPos = pos - self._startPos
            self._startPos = pos
            self.data['position'] = (self.data['position'][0] + relPos.x(), self.data['position'][1] + relPos.y())

    def mouseReleaseEvent(self, event):
        self._mousePressed = False
        self.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
