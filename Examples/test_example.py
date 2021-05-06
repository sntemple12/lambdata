from random import randint
import pytest
from example import increment, COLORS

def test_increment():
    assert increment(3) ==5