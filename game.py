from ai import AI
from human import Human


class Game:
    def __init__(self):  # need to create option for two players or one player
        self.player_one = Human()
        self.player_two = AI()
        self.player_three = Human()

    def display_welcome(self):
        print("Welcome to Rock, Paper, Scissors but with a twist! Now Introducing Spock and Lizard!")
        print("Rules:\n Rock crushes Scissors \n Scissors cuts Paper \n Paper covers Rock \n Rock crushes Lizard \n Lizard poisons Spock \n Spock smashes Scissors \n Scissors decapitates Lizard \n")
        print("Let's Get Started!")

    def multiplayer(self):
        user_input = input(
            "Press 1: Player vs CPU \n Press 2: Player vs Player ")
        if user_input == 1:
            pass
        # set player two from AI to human.
        elif user_input == 2:
            pass

    def game_rounds():
        # Add algorithm to calculate what round is being played.
        pass

    def compare_scores():
        # Algorithm to calculate the total number of wins each player has and compare them to see who is winning/won.
        pass

    def display_winner():
        # if player_one wins is larger than player two wins.
        # then player one wins
        # else if player two is the winner.
        pass

    def run_game(self):
        self.display_welcome()
        self.multiplayer()
        self.display_winner()
