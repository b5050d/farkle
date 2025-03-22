"""
Written by b5050d

3.20.2025

Dice implementation
"""

import numpy as np


def dice_roll():
    """
    Return an integer representing the value of a dice roll
    """
    return np.random.randint(1, 7)


class Dice:
    """
    Class to handle Dice implementation
    """

    def __init__(self):
        """
        Set up the class
        """
        self.value = dice_roll()

    def roll(self):
        """
        Roll this dice, update its value
        """
        self.value = dice_roll()
        return self.value
