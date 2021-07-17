from ai import AI
from human import Human

# added player scores to be set to 0 to allow for calculating wins.
player_one_score = 0
player_two_score = 0


class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = ""  # create option for player two to be a human or AI

    def display_welcome(self):
        print("Welcome to Rock, Paper, Scissors but with a twist! Now Introducing Spock and Lizard!")
        print("Rules:\n Rock crushes Scissors \n Scissors cuts Paper \n Paper covers Rock \n Rock crushes Lizard \n Lizard poisons Spock \n Spock smashes Scissors \n Scissors decapitates Lizard \n Best of three rounds wins! \n")
        print("Let's Get Started!")

    def game_mode(self):
        user_input = input(
            "Press 1: Player vs CPU\nPress 2: Player vs Player\n")
        if user_input == 1:
            self.player_one = Human()
            self.player_two = AI()
        # set player two from AI to human.
        elif user_input == 2:
            self.player_one = Human()
            self.player_two = Human()

# TODO: finish comparing player one and player two gestures/round.
    def single_player(self):
        global player_one_score
        global player_two_score
        self.player_one_turn =
        self.player_two_turn =
        pass
# TODO: finish comparing player one and player two gestures/round.

    def multiplayer(self):
        global player_one_score
        global player_two_score
        self.player_one_turn =
        self.player_two_turn =
        if self.player_one == self.player_two:
            print("Tie")

    def game_rounds(self):
        print("You will need to win 2 rounds to be the overall Winner!")

    def compare_scores(self):
        while player_one_score < 2 and player_two_score < 2:
            if player_one_score == 2:
                print("WINNER! WINNER! CHICKEN DINNER!")
            else:
                print("Player ... Wins!")
                return self.game_rounds
            pass

    def display_winner(self):
        # if player_one wins is larger than player two wins.
        # then player one wins
        # else if player two is the winner.
        pass

    def run_game(self):
        self.display_welcome()
        self.game_mode()
        self.game_rounds()
        self.display_winner()
        self.multiplayer()
