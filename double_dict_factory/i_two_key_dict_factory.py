import abc
from typing import Callable
from typing import TypeVar, Generic

FACTORY_KEY = TypeVar('FACTORY_KEY')
TRIGGER_KEY = TypeVar('TRIGGER_KEY')
OBJECT = TypeVar('OBJECT')


class ITwoKeyDictFactory(Generic[FACTORY_KEY, TRIGGER_KEY, OBJECT], metaclass=abc.ABCMeta):

    def add_factory(self, factory_key: FACTORY_KEY, factory: Callable[[], OBJECT]):
        raise NotImplementedError

    def remove_factory(self, factory_key: FACTORY_KEY):
        raise NotImplementedError

    def create(self, trigger_key: TRIGGER_KEY):
        raise NotImplementedError

    def remove(self, trigger_key: TRIGGER_KEY):
        raise NotImplementedError

    def get(self, trigger_key: TRIGGER_KEY, factory_key: FACTORY_KEY) -> OBJECT:
        raise NotImplementedError
