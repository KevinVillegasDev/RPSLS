class Player:
    def __init__(self):
        self.name = input("What is your name?")
        self.gesture = self.create_gesture()
        self.score = 0

    def create_gesture(self):
        self.gesture = ["rock", "paper", "scissors", "spock", "lizard"]
        return self.gesture

    def select_gesture(self):
        self.choose_gesture = int(input(
            "What gesture do you choose? 1 = rock, 2 = paper, 3 = scissors, 4 = spock, 5 = lizard"))
        if self.choose_gesture == 1:
            self.choose_gesture = "rock"
        elif self.choose_gesture == 2:
            self.choose_gesture = "paper"
        elif self.choose_gesture == 3:
            self.choose_gesture = "scissors"
        elif self.choose_gesture == 4:
            self.choose_gesture = "spock"
        elif self.choose_gesture == 5:
            self.choose_gesture = "lizard"
        
