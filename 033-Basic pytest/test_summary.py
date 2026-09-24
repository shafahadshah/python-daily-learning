from calculator import add
from greeting import greet


def test_calculator():
    assert add(10, 5) == 15


def test_greeting():
    assert greet("Sara") == "Hello, Sara"