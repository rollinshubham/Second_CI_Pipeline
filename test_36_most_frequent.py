import importlib

module = importlib.import_module("36_most_frequent")


def test_most_frequent():
    assert module.most_frequent([1, 3, 1, 3, 2, 1]) == 1


def test_single_element():
    assert module.most_frequent([5]) == 5


def test_empty_list():
    assert module.most_frequent([]) is None


def test_negative_numbers():
    assert module.most_frequent([-1, -2, -1, -3]) == -1