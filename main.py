# Step 1- Start the game
# Step 2- Display rules of the game
# Step 3- Ask user if game will be played in 1 player vs AI or 2 player
# Step 4- Display a list of gesture options
# Step 5- First player will choose a gesture
# Step 6- Second player will choose a gesture
# Step 7- Both gestures will be displayed
# Step 8- Winning gesture will be determined and round winner displayed and track the score (check for ties)
# Step 9- Prompt players for new gestures for second round
# Step 10- Repeat step 4, 5, 6, 7 two more times
# Step 11- If any player wins first two rounds, display match winner and skip round 3

from player import Player
from ai import AI



round_one = Player()
round_one.select_gesture()

robot = AI()
robot.get_gesture()

print("The end")


