from double_dict_factory import TwoKeyDictFactory, ITwoKeyDictFactory


def factory1():
    return 10


def factory2():
    return 20


def test_create():
    two_key_dict: ITwoKeyDictFactory[int, int, int] = TwoKeyDictFactory()
    two_key_dict.add_factory(1, factory1)
    two_key_dict.add_factory(2, factory2)
    two_key_dict.create(10)

    assert two_key_dict.get(10, 1) == 10
    assert two_key_dict.get(10, 2) == 20

    a = 1


class DummyClassFce2:
    index = 0

    def __init__(self):
        DummyClassFce2.index += 1
        self.index = DummyClassFce2.index


def test_created_once():
    two_key_dict = TwoKeyDictFactory()
    two_key_dict.add_factory(10, DummyClassFce2)
    two_key_dict.create(1)
    two_key_dict.create(1)
    assert DummyClassFce2.index == 1
    two_key_dict.create(2)
    assert DummyClassFce2.index == 2


def test_get_will_create_trigger_key():
    two_key_dict = TwoKeyDictFactory()
    two_key_dict.add_factory(10, factory1)
    two_key_dict.add_factory(20, factory2)
    two_key_dict.create(1)
    assert two_key_dict.get(1, 10) == 10
    assert two_key_dict.get(2, 20) == 20


def test_removed_multiple_times():
    two_key_dict = TwoKeyDictFactory()
    two_key_dict.add_factory(10, factory1)
    two_key_dict.add_factory(20, factory2)
    two_key_dict.create(1)
    assert two_key_dict.get(1, 10) == 10
    two_key_dict.remove(1)
    two_key_dict.remove(1)
    two_key_dict.remove(1)
