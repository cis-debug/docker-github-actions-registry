"""
test_app.py
Tests automatiques pour app.py (pytest).
"""

from app import add, greet


def test_add():
    assert add(2, 3) == 5


def test_greet():
    assert greet("World") == "Hello World!"
