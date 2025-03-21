import numpy as np


def dice_roll():
    """
    Return an integer representing the value of a dice roll
    """
    return np.random.randint(1, 7)


class Dice:
    def __init__(self):
        self.value = dice_roll()

    def roll(self):
        self.value = dice_roll()
        return self.value

class Turn:
    def __init__(self):
        # self.active_dice = 6
        self.active_dice = []
        for i in range(6):
            self.active_dice.append(Dice())

        self.score = 0

        self.bust = False
        self.end = False

    def roll(self):
        for iter, d in enumerate(self.active_dice):
            value = d.roll()
            print(f"Dice {iter} reads : {value}")

    def process_turn(self):
        while not self.bust and not self.end:
            if len(self.active_dice) == 0:
                print("")
                print("You used all the dice! You get 6 fresh ones")
                for i in range(6):
                    self.active_dice.append(Dice())
            print("")
            print("Rolling Dice")
            # if there are 0 dice left, then roll 6 again!
            a.roll()
            indexes = self.ask_which_to_score()
            if indexes == None:
                break
            score = self.calculate_score(indexes)

            # print("Indexes: {}".format(indexes))
            # Remove the dice
            for index in indexes[::-1]:
                del self.active_dice[index]

            roll_again = input(f"Roll again with {len(self.active_dice)}?(y/n)")
            if roll_again == "y":
                pass
            else:
                self.end = True
        if self.end:
            print(f"Ended turn with score: {self.score}")

    def ask_which_to_score(self):
        while True:
            to_score = input("Enter which dice to score:")
            if to_score == "":
                self.act_bust()
                return None
            break

        if to_score == "":
            print("User did not enter any dice to score, ending turn!")
            self.end = True
            return
        # parse toscore
        dice_indexes_to_score = [int(i) for i in to_score.split(",")]

        if 7 in dice_indexes_to_score:
            self.end = True
            dice_indexes_to_score.remove(7)

        return dice_indexes_to_score

    def act_bust(self):
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

        print(values)

        # Check if its 6 in a row:
        values = sorted(values)

        # Check for 5 in a row:

        # Check for 4 in a row:

        # Check for 3 in a row:

        # Check for 1s and 5s:
        print("Selected Values: {}".format(values))
        score = int(input("Whats the score?:"))
        if score == 0:
            self.bust = True

        print(f"Scored: {score}")
        self.score += score
        print("Turn score now: {}".format(self.score))



if __name__ == "__main__":
    a = Turn()
    a.process_turn()
