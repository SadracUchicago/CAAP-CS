# YOUR NAME
# ASSIGNMENT

from random import randint

# global variable of chutes and ladders
# remember to let your function know you're using this variable with 'global'
chutes_ladders = {4 : 7,
                    8 : 15,
                    12 : 2,
                    14: 6}

# Rolls a die of six sides and returns the result
def roll_die():
    dice_roll = randint(1, 6)
    return dice_roll
roll_die()
# makes a game (just a list) of the given dimensions
def makeGame(w, l):
    List = list(range(w, l))
    return List


# checks if given square is a chutes or ladders
def is_chutes_ladders(d):
    for i in List:
        print(i)
# function to make and play a game
def play_game():
    state = # This should be a list of dictionaries of each player's state
    mode = 'pc' # or 'user'
    raise ValueError("todo")

# Runs the game as a simulation and keeps track of the number of moves it takes to win and returns average
def simulate_game():
    raise ValueError("todo")