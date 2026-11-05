import importlib

module = importlib.import_module("40_gcd")


def test_gcd():
    assert module.gcd(12, 18) == 6


def test_gcd_coprime():
    assert module.gcd(7, 9) == 1


def test_gcd_same_numbers():
    assert module.gcd(10, 10) == 10


def test_gcd_with_zero():
    assert module.gcd(15, 0) == 15