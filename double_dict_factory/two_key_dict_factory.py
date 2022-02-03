from typing import Callable

# from . import ITwoKeyDictFactory
from typing import TypeVar, Generic

from double_dict_factory import ITwoKeyDictFactory

FACTORY_KEY = TypeVar('FACTORY_KEY')
TRIGGER_KEY = TypeVar('TRIGGER_KEY')
OBJECT = TypeVar('OBJECT')


class TwoKeyDictFactory(Generic[FACTORY_KEY, TRIGGER_KEY, OBJECT],
                        ITwoKeyDictFactory[FACTORY_KEY, TRIGGER_KEY, OBJECT]):
    def __init__(self):
        self._factories: dict[FACTORY_KEY, Callable[[], OBJECT]] = {}
        self._objects: dict[TRIGGER_KEY, dict[FACTORY_KEY, OBJECT]] = {}

    def add_factory(self, factory_key: FACTORY_KEY, factory: Callable[[], OBJECT]):
        self._factories[factory_key] = factory

    def remove_factory(self, factory_key: FACTORY_KEY):
        self._factories.pop(factory_key)

    def create(self, trigger_key: TRIGGER_KEY):
        if trigger_key not in self._objects:
            new_objects: dict[FACTORY_KEY, OBJECT] = {}
            for key1, factory in self._factories.items():
                new_objects[key1] = factory()
            self._objects[trigger_key] = new_objects

    def remove(self, trigger_key: TRIGGER_KEY):
        if trigger_key in self._objects:
            self._objects.pop(trigger_key)

    def get(self, trigger_key: TRIGGER_KEY, factory_key: FACTORY_KEY) -> OBJECT:
        if trigger_key not in self._objects:
            self.create(trigger_key)
        return self._objects[trigger_key][factory_key]
