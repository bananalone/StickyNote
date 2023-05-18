from typing import Dict, Any

from QtHelper._Refreshable import Refreshable


class Data:
    def __init__(self, data: Dict[str, Any]):
        self._data = data.copy()  # 数据
        self._refreshableItems = set()  # 所有监听此数据得视图

    @staticmethod
    def builder(data: Dict[str, Any]):

        def create(**kwargs):
            clone = data.copy()
            for key in kwargs:
                Data._checkKey(clone, key)
            clone.update(**kwargs)
            return Data(clone)

        return create

    def mount(self, refreshableItem: Refreshable) -> 'Data':
        self._refreshableItems.add(refreshableItem)
        return self

    def __getitem__(self, key: str):
        Data._checkKey(self._data, key)
        return self._data[key]

    def __setitem__(self, key: str, value: Any):
        Data._checkKey(self._data, key)
        self._data[key] = value
        self._refresh()

    def __str__(self):
        return str(self._data)

    @property
    def data(self) -> Dict[str, Any]:
        return self._data.copy()

    def update(self, data: Dict[str, Any]):
        for key in data:
            Data._checkKey(self._data, key)
        self._data.update(data)
        self._refresh()

    def _refresh(self):
        for refreshableItem in self._refreshableItems:
            refreshableItem.refresh()

    @staticmethod
    def _checkKey(data: Dict[str, Any], key: str):
        if key not in data:
            raise Exception(f'{key} is not an attribute of Data')
