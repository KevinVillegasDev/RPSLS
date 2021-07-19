class Player:
    def __init__(self, name):
        self.name = name
        self.gesture = self.create_gesture()
        self.score = 0

    def create_gesture(self):
        self.gesture = ["rock", "paper", "scissors", "spock", "lizard"]
        return self.gesture

    def choose_gesture(self):
        isValid = False
        while isValid == False:
            self.chosen_gesture = input(
                "What gesture do you choose? 1 = rock, 2 = paper, 3 = scissors, 4 = spock, 5 = lizard \n")
            if self.chosen_gesture == "1":
                self.chosen_gesture = "rock"
                isValid = True
            elif self.chosen_gesture == "2":
                self.chosen_gesture = "paper"
                isValid = True
            elif self.chosen_gesture == "3":
                self.chosen_gesture = "scissors"
                isValid = True
            elif self.chosen_gesture == "4":
                self.chosen_gesture = "spock"
                isValid = True
            elif self.chosen_gesture == "5":
                self.chosen_gesture = "lizard"
                isValid = True
            else:
                print("Not a valid Selection")
        print("Player has selected " + self.chosen_gesture)
        return self.chosen_gesture
    
