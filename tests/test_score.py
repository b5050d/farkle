"""
Written by b5050d

3.21.2025

Testing script for calculation of the score
"""

import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)

from farkle.score import calculate_score

def test_score():
    """
    Test the scoring function
    """
    ans = calculate_score([1])
    assert ans == 100

    ans = calculate_score([5])
    assert ans == 50

    ans = calculate_score([1, 5])
    assert ans == 150

    ans = calculate_score([1, 1])
    assert ans == 200

    ans = calculate_score([5, 5])
    assert ans == 100

    ans = calculate_score([1, 1, 5, 5])
    assert ans == 300

    ans = calculate_score([1, 2, 3, 4, 5, 6])
    assert ans == 1500

    ans = calculate_score([1, 1, 1])
    assert ans == 1000

    ans = calculate_score([2, 2, 2])
    assert ans == 200

    ans = calculate_score([3, 3, 3])
    assert ans == 300

    ans = calculate_score([4, 4, 4])
    assert ans == 400

    ans = calculate_score([5, 5, 5])
    assert ans == 500

    ans = calculate_score([6, 6, 6])
    assert ans == 600

    ans = calculate_score([2, 2, 2, 4, 4, 4])
    assert ans == 2500

    ans = calculate_score([2, 2, 1, 3, 3, 1])
    assert ans == 1500

    # ans = calculate_score([1, 2, 3, 4, 5, 3])
    # assert ans == 1500

    # ans = calculate_score([1, 2, 3, 4, 5, 5])
    # assert ans == 1550

    # ans = calculate_score([1, 2, 3, 4, 5, 1])
    # assert ans == 1600

    # ans = calculate_score([2, 2, 3, 4, 5, 6])
    # assert ans == 1500

    print("Tests Passed!")


if __name__ == "__main__":
    test_score()
