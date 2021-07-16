from player import Player
import random


class AI(Player):
    def __init__(self):
        self.name = "Computer"
        super().__init__()

    def get_gesture(self):
        self.choice = self.gesture[random.randint(1, 5)]
        print("The computer selects:" + self.choice)
