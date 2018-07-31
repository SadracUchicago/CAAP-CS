# Sadrac Camacho
# Lab3

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
    current_player_value = []
    if mode == 'real':
        players = int(input("How many players?: "))
        question = input("\nGo Further? [press enter...]: ")
        dice = 0
        position = 1
        for i in range(players):
            current_player_value.append(
                {'player_name': input('Player ' + str(i + 1) + " What is your name?: "), 'value': 1, 'moves': 0})

        while question.upper() == '':
            for i in range(players):
                playah = current_player_value[i]['player_name']
                current_player_value[i]['moves'] += 1
                dice += roll_die()
                print('\n' + playah, "your dice is", dice)
                position += (current_player_value[i]['value'] + dice) - 1
                if position in chutes_ladders:
                    if position > chutes_ladders.get(position):
                        position = chutes_ladders.get(position)
                        current_player_value[i]['value'] = position

                        print("You fell into a chute; your position is now", current_player_value[i]['value'])
                    else:
                        position = chutes_ladders.get(position)
                        current_player_value[i]['value'] = position
                        print("You climbed up a ladder; your position is now", current_player_value[i]['value'])
                else:
                    current_player_value[i]['value'] = position
                    print("Your position is", position)

                if position >= 36:
                    print("That position means", playah, "WON!!!")
                    print("moves to win", current_player_value[i]['moves'])
                    return
                question = input("\nNext player roll...")
                dice = 0
                position = 1
    elif mode == 'pc':
        dice = 0
        position = 1
        loop = True
        count = 0

        while loop == True:
            count += 1
            dice += randint(1, 6)
            # print("Your dice is", dice)
            position += dice
            if position in chutes_ladders:
                position = chutes_ladders.get(position)
            else:
                pass
            # print("Your position is ", position)

            dice = 0

            if position >= 36:
                # print("You went over 36 and have won!!!")
                break
        # print("It took these many moves to win: ", count)
        return count


# play_game('pc')

def simulate_game():
    that = []
    num = int(input("How many tests [10 OR 100 OR 1,000 OR 10,000 OR 100,000: "))
    for i in range(0, num):
        that.append(play_game('pc'))
    print(that)
    average = (sum(that) / num)
    print(average)
    return average


simulate_game()
