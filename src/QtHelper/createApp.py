from QtHelper.Data import Data
from QtHelper.View import View


class _App:
    def __init__(self, data: Data):
        self._data = data

    def mount(self, view: View) -> '_App':
        view.bind(self._data)
        self._data.mount(view)
        return self


def createApp(data: Data):
    return _App(data)
