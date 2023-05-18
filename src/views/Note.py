import json
from pathlib import Path

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from QtHelper import View, createApp
import data
from views.MenuBar import MenuBar
from views.TextEdit import TextEdit


class Note(QWidget, View):
    def __init__(self, dataPath: str):
        super().__init__()
        noteData = data.Note()
        self._dataPath = Path(dataPath)
        if self._dataPath.exists():
            loadData = json.loads(self._dataPath.read_text())
            noteData.update(loadData)
            noteData['close'] = False
        self._menuBar = MenuBar()
        self._textEdit = TextEdit(noteData['text'])
        vbox = QVBoxLayout()
        vbox.addWidget(self._menuBar)
        vbox.addWidget(self._textEdit)
        vbox.setSpacing(0)
        vbox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(vbox)
        self.setMinimumSize(360, 180)
        self.setWindowTitle('StickNote')
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMinimumSize(360, 360)
        self._ctrlPressed = False
        self._shiftPressed = False
        self._INCREMENT = 50
        createApp(noteData).mount(self).mount(self._menuBar).mount(self._textEdit)

    def display(self):
        print(f'Note {self.data}')
        self.move(self.data['position'][0], self.data['position'][1])
        self.resize(self.data['size'][0], self.data['size'][1])
        if self.data['close']:
            dumpData = json.dumps(self.data.data)
            self._dataPath.write_text(dumpData)
            self.close()
        if self.data['showMinimized']:
            self.data['showMinimized'] = False
            self.showMinimized()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Control:
            self._ctrlPressed = True
        if event.key() == Qt.Key.Key_Shift:
            self._shiftPressed = True

    def keyReleaseEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Control:
            self._ctrlPressed = False
        if event.key() == Qt.Key.Key_Shift:
            self._shiftPressed = False

    def wheelEvent(self, event: QWheelEvent) -> None:
        if not self._ctrlPressed:
            return
        if event.angleDelta().y() > 0:
            if self._shiftPressed:
                self.data['size'] = (self.data['size'][0] + self._INCREMENT, self.data['size'][1])
            else:
                self.data['size'] = (self.data['size'][0], self.data['size'][1] + self._INCREMENT)
        else:
            if self._shiftPressed:
                self.data['size'] = (self.data['size'][0] - self._INCREMENT, self.data['size'][1])
            else:
                self.data['size'] = (self.data['size'][0], self.data['size'][1] - self._INCREMENT)

