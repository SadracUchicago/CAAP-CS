# YOUR NAME
# ASSIGNMENT

from random import randint

# global variable of chutes and ladders
# remember to let your function know you're using this variable with 'global'
chutes_ladders = {4: 7,
                  8: 15,
                  12: 2,
                  14: 6}


# Rolls a die of six sides and returns the result
def roll_die():
    dice_roll = randint(1, 6)
    return dice_roll


roll_die()


# makes a game (just a list) of the given dimensions

def makeGame():
    List = list(range(1, 37))
    return List


# checks if given square is a chutes or ladders
def is_chutes_ladders():
    for i in makeGame():
        if i in chutes_ladders.keys():
            if i > int(chutes_ladders.get(i)):
                print(i, "Shoot")
            elif i < int(chutes_ladders.get(i)):
                print(i, "Ladder")
        else:
            pass


# function to make and play a game
def play_game(mode):
    if mode == 'real':
        Players = int(input("How many players?: "))
    question = input(" Go Further?: Y or N : ")
    dice = 0
    position = 1
    while question.upper() == 'Y':
        dice += roll_die()
        print("Your dice is", dice)
        position += dice

        if position in chutes_ladders:
            if position > chutes_ladders.get(position):
                position = chutes_ladders.get(position)
                print("You fell into a chute; your position is now", position)
            else:
                position = chutes_ladders.get(position)
                print("You climbed up a ladder; your position is now", position)
        else:
            print("Your position is ", position)

        if position >= 36:
            print("You went over 36 and have won!!!")
            break
        else:
            pass
        question = input("Do you want to roll again?: ")
        dice = 0


play_game('user')


# Runs the game as a simulation and keeps track of the number of moves it takes to win and returns average
# def simulate_game():
#    raise ValueError("todo")
