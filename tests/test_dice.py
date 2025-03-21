"""
Written by b5050d

3.20.2025
"""

import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)

from farkle.dice import dice_roll, Dice


def test_roll_dice():
    """
    Test that the dice roll works
    """
    for i in range(10):
        ans = dice_roll()
        assert ans > 0
        assert ans < 7
        assert type(ans) is int


def test_dice_class():
    """
    Check that the dice class comes up
    """
    a = Dice()
    assert a.value > 0
    assert a.value < 7
    assert type(a.value) is int

    a.roll()
    assert a.value > 0
    assert a.value < 7
    assert type(a.value) is int
    