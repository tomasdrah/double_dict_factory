def factory1():
    return 10


def factory2():
    return 20


def test_create():
    from double_dict_factory import TwoKeyDictFactory, ITwoKeyDictFactory

    two_key_dict: ITwoKeyDictFactory[int, int, int] = TwoKeyDictFactory()
    two_key_dict.add_factory(1, factory1)
    two_key_dict.add_factory(2, factory2)
    two_key_dict.create(10)

    assert two_key_dict.get(10, 1) == 10
    assert two_key_dict.get(10, 2) == 20

    a = 1
