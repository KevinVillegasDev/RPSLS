from ai import AI
from human import Human





class Game:
    def __init__(self):
        self.player_one = Human(self)
        self.player_two = None
        self.ai = AI()
          

    def display_welcome(self):
        print("Welcome to Rock, Paper, Scissors but with a twist! Now Introducing Spock and Lizard!")
        print("Rules:\n Rock crushes Scissors \n Scissors cuts Paper \n Paper covers Rock \n Rock crushes Lizard \n Lizard poisons Spock \n Spock smashes Scissors \n Scissors decapitates Lizard \n Lizard eats Paper \n Paper disproves Spock \n Spock Vaporizes Rock \n Best of three rounds wins! \n")
        print("Let's Get Started!")

    def game_mode(self):
        user_input = input(
            "Press 1: Player vs CPU\nPress 2: Player vs Player\n")
        if user_input == "1":
            self.player_one = Human("Bob")
            self.player_two = AI()
        elif user_input == "2":
            self.player_one = Human("Bob")
            self.player_two = Human("Frank")
        else:
            self.player_one = AI()
            self.player_two = AI()
        self.compare_scores_single_player()
        self.display_winner_single_player()


    def single_player(self):
        self.player_one_turn = self.player_one.choose_gesture()
        self.player_two_turn = self.player_two.choose_gesture()
        
        #self.player_one.chosen_gesture.compare(self.player_two.chosen_gesture)
        if self.player_one_turn == self.player_two_turn:
             print("Round tie!")
        elif self.player_one_turn == "rock" and self.player_two_turn == "scissors":
            print("Player one wins the round!")
            self.player_one.score += 1
        elif self.player_one_turn == "paper" and self.player_two_turn == "rock":
            print("Player one wins the round!")
            self.player_one.score += 1
        elif self.player_one_turn == "scissors" and self.player_two_turn == "paper":
            print("Player one wins the round!")
            self.player_one.score += 1
        elif self.player_one_turn == "rock" and self.player_two_turn == "lizard":
            print("Player one wins the round!")
            self.player_one.score += 1
        elif self.player_one_turn == "lizard" and self.player_two_turn != "spock":
            print("Player one wins the round!")
            self.player_one.score += 1
        elif self.player_one_turn == "spock" and self.player_two_turn == "scissors":
            print("Player one wins the round!")
            self.player_one.score += 1
        elif self.player_one_turn == "scissors" and self.player_two_turn == "lizard":
            print("Player one wins the round!")
            self.player_one.score += 1
        elif self.player_one_turn == "lizard" and self.player_two_turn == "paper":
            print("Player one wins the round!")
            self.player_one.score += 1
        elif self.player_one_turn == "paper" and self.player_two_turn == "spock":
            print("Player one wins the round!")
            self.player_one.score += 1
        elif self.player_one_turn == "spock" and self.player_two_turn == "rock":
            print("Player one wins the round!")
            self.player_one.score += 1
        else:
            print("Computer wins the round!")
            self.player_two.score += 1
        print(f'Player 1 has a score of {self.player_one.score}' )
        print(f'The computer has a score of {self.player_two.score}')




    

    def game_rounds(self):
        print("You will need to win 2 rounds to be the overall Winner!")

    def compare_scores_single_player(self):
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.single_player()
    
    

    def display_winner_single_player(self):
        if self.player_one.score == 2:
                print("Player 1: WINNER! WINNER! CHICKEN DINNER!")
        elif self.player_two.score == 2:
                print("Computer Wins!")
    
                

    def run_game(self):
        self.display_welcome()
        self.game_rounds()
        self.game_mode()
