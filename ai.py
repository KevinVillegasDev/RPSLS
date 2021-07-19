from player import Player
import random


class AI(Player):
    def __init__(self):
        super().__init__(self)

    def get_gesture(self):
        self.choice = random.randint(1,5)
        if self.choice == 1:
            self.choice = "rock"
        elif self.choice == 2:
            self.choice = "paper"
        elif self.choice == 3:
            self.choice = "scissors"
        elif self.choice == 4:
            self.choice = "spock"
        elif self.choice == 5:
            self.choice = "lizard"
        print("The computer selects: " + self.choice)
        return self.choice
