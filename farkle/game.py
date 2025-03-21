"""
Written by b5050d

3.20.2025
"""

from farkle.turn import Turn

class Game:

    def __init__(self, winning_score = 2000):
        """
        Set up the class
        """
        self.winning_score = winning_score

        # Assume 2 players
        self.scores = [0, 0]

    def main_loop(self):
        """
        Main functionality
        """
        player_index = 0
        while max(self.scores) < self.winning_score:
            # Start a turn
            print(f"Starting Turn for Player: {player_index}")

            turn = Turn()
            turn.main_loop()

            self.scores[player_index] += turn.score
            turn = None # Clear the turn

            print("End of Turn")
            print(f"Player 0 score: {self.scores[0]}")
            print(f"Player 1 score: {self.scores[1]}")
            print("")

            if player_index == 0: player_index = 1
            else: player_index = 0

        print("Game has ended!")
        print(f"Player {player_index} has won! {self.scores[player_index]} points")


