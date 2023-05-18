from QtHelper._Refreshable import Refreshable
from QtHelper.Data import Data


class View(Refreshable):
    def __init__(self):
        self.data: Data = Data({})
        self._bind = False
        self._isDisplaying = False

    def display(self):
        raise NotImplementedError

    def bind(self, data: Data):
        self.data = data
        self._bind = True
        self.refresh()

    def refresh(self):
        if not self._bind:
            raise Exception('No data is bound to the view')
        if not self._isDisplaying:  # 保证每次修改只刷新一次, 预防递归刷新
            self._isDisplaying = True
            self.display()
            self._isDisplaying = False
