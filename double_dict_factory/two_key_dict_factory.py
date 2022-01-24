from typing import Callable

# from . import ITwoKeyDictFactory
from typing import TypeVar, Generic

from double_dict_factory import ITwoKeyDictFactory

KEY1 = TypeVar('KEY1')
KEY2 = TypeVar('KEY2')
OBJECT = TypeVar('OBJECT')


class TwoKeyDictFactory(Generic[KEY1, KEY2, OBJECT], ITwoKeyDictFactory[KEY1, KEY2, OBJECT]):
    def __init__(self):
        self._factories: dict[KEY1, Callable[[], OBJECT]] = {}
        self._objects: dict[KEY2, dict[KEY1, OBJECT]] = {}

    def add_factory(self, object_key1: KEY1, factory: Callable[[], OBJECT]):
        self._factories[object_key1] = factory

    def remove_factory(self, object_key1: KEY1):
        self._factories.pop(object_key1)

    def create(self, key2: KEY2):
        new_objects: dict[KEY1, OBJECT] = {}
        for key1, factory in self._factories.items():
            new_objects[key1] = factory()
        self._objects[key2] = new_objects

    def remove(self, key2: KEY2):
        self._objects.pop(key2)

    def get(self, key2: KEY2, object_key1: KEY1) -> OBJECT:
        return self._objects[key2][object_key1]
