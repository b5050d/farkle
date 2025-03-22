"""
Written by b5050d

3.20.2025
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from farkle.turn import Turn


def test_turn_init():
    """
    Test that the turn class comes up ok
    """
    a = Turn()

    assert a.score == 0
    assert len(a.active_dice) == 6
    assert a.bust is False
    assert a.end is False


def test_turn_enact_bust():
    a = Turn()
    a.score = 100
    assert a.score == 100
    assert a.bust is False

    a.enact_bust()
    assert a.score == 0
    assert a.bust is True
