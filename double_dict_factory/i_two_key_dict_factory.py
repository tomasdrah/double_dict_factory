import abc
from typing import Callable
from typing import TypeVar, Generic

KEY1 = TypeVar('KEY1')
KEY2 = TypeVar('KEY2')
OBJECT = TypeVar('OBJECT')


class ITwoKeyDictFactory(Generic[KEY1, KEY2, OBJECT], metaclass=abc.ABCMeta):

    def add_factory(self, object_key1: KEY1, factory: Callable[[], OBJECT]):
        raise NotImplementedError

    def remove_factory(self, object_key1: KEY1):
        raise NotImplementedError

    def create(self, key2: KEY2):
        raise NotImplementedError

    def remove(self, key2: KEY2):
        raise NotImplementedError

    def get(self, key2: KEY2, object_key1: KEY1) -> OBJECT:
        raise NotImplementedError
