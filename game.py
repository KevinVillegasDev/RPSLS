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
        print("Rules:\n Rock crushes Scissors \n Scissors cuts Paper \n Paper covers Rock \n Rock crushes Lizard \n Lizard poisons Spock \n Spock smashes Scissors \n Scissors decapitates Lizard \n Lizard eats Paper \n Paper disproves Spock \n Spock Vaporizes Rock '\n*2' Best of three rounds wins! \n")
        print("Let's Get Started!")

    def game_mode(self):
        user_input = input(
            "Press 1: Player vs CPU\nPress 2: Player vs Player\n")
        if user_input == 1:
            self.player_one = Human()
            self.player_two = AI()
            self.single_player()
        # set player two from AI to human.
        elif user_input == 2:
            self.player_one = Human()
            self.player_two = Human()
            self.multiplayer()

# TODO: finish comparing player one and player two gestures/round.
    def single_player(self):
        global player_one_score
        global player_two_score
        self.player_one_turn = Human().select_gesture
        self.player_two_turn = AI().get_gesture
        if self.player_one_turn == self.player_two_turn:
            print("Round tie!")
        elif self.player_one_turn == "rock" and self.player_two_turn == "scissors":
            print("Player one wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "paper" and self.player_two_turn == "rock":
            print("Player one wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "scissors" and self.player_two_turn == "paper":
            print("Player one wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "rock" and self.player_two_turn == "lizard":
            print("Player one wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "lizard" and self.player_two_turn != "spock":
            print("Player one wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "spock" and self.player_two_turn == "scissors":
            print("Player one wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "scissors" and self.player_two_turn == "lizard":
            print("Player one wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "lizard" and self.player_two_turn == "paper":
            print(" Player one wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "paper" and self.player_two_turn == "spock":
            print(" Player one wins the round!")
            player_one_score += 1
        elif self.player_one_turn == "spock" and self.player_two_turn == "rock":
            print(" Player one wins the round!")
            player_one_score += 1
        else:
            print("Player Two wins the round!")
            player_two_score += 1


# TODO: finish comparing player one and player two gestures/round.

    def multiplayer(self):
        global player_one_score
        global player_two_score
        self.player_one_turn = Human().select_gesture
        self.player_two_turn = Human().select_gesture
        if self.player_one_turn == self.player_two_turn:
            print("Tie")
            pass

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
