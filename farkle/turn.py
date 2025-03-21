"""
Written by b5050d

3.20.2025

Turn for the dice
"""

from farkle.dice import Dice


class Turn:
    """
    Class to handle a user's turn
    """

    def __init__(self):
        """
        Set up the class
        """
        self.score = 0
        self.bust = False
        self.end = False
        
        self.active_dice = []
        for i in range(6):
            self.active_dice.append(Dice())

    def __repr__(self):
        """
        Represent the turn as a string
        """
        answer = ""
        answer += "Turn information:\n"
        answer += f"Current Score: {self.score}\n"
        answer += f"Active Dice: {len(self.active_dice)}\n"
        return answer
    
    def _roll(self):
        """
        Roll all of the active dice
        """
        for iter, d in enumerate(self.active_dice):
            value = d.roll()
            print(f"Dice {iter} reads : {value}")

    def ask_which_to_score(self):
        """
        Ask the user which dice to score
        """
        while True:
            to_score = input("Enter which dice to score:")
            if to_score == "":
                self.enact_bust()
                return None
            break

        if to_score == "":
            print("User did not enter any dice to score, ending turn!")
            self.end = True
            return

        dice_indexes_to_score = [int(i) for i in to_score.split(",")]

        if 7 in dice_indexes_to_score:
            self.end = True
            dice_indexes_to_score.remove(7)

        return dice_indexes_to_score

    def enact_bust(self):
        """
        Enact a bust
        """
        print("You busted! Your score for this turn is lost!")
        self.bust = True
        self.score = 0
        return None

    def calculate_score(self, to_score):
        """
        Calculate the score of the selected dice
        """
        values = []
        for didx in to_score:
            assert didx in [0, 1, 2, 3, 4, 5]

            # get the value
            value = self.active_dice[didx].value
            values.append(value)

        values = sorted(values)

        print("Selected Values: {}".format(values))
        score = int(input("Whats the score?:"))
        if score == 0:
            self.bust = True

        print(f"Scored: {score}")
        self.score += score
        print("Turn score now: {}".format(self.score))

    def main_loop(self):
        """
        Process the user's turn
        """
        while not self.bust and not self.end:
            if len(self.active_dice) == 0:
                print("")
                print("You used all the dice! You get 6 fresh ones")
                for i in range(6):
                    self.active_dice.append(Dice())
            print("")
            print("Rolling Dice")
            # if there are 0 dice left, then roll 6 again!
            self._roll()
            indexes = self.ask_which_to_score()
            if indexes == None:
                break
            score = self.calculate_score(indexes)

            # Remove the dice that were scored
            for index in indexes[::-1]:
                del self.active_dice[index]

            roll_again = input(f"Roll again with {len(self.active_dice)}?(y/n)")
            if roll_again == "y":
                pass
            else:
                self.end = True
        if self.end:
            print(f"Ended turn with score: {self.score}")

