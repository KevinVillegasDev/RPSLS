from player import Player
import random


class AI(Player):
    def __init__(self):
        super().__init__(self)

    def get_gesture(self):
        self.choice = random.choice(self.choose_gesture)
        print("The computer selects: " + self.choice)
