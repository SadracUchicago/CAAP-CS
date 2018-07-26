from random import randint

List = list(range(1, 37))
print(List)

chutes_ladders = {4: 7,
                  8: 15,
                  12: 2,
                  14: 6}

for i in List:
    if i in chutes_ladders.keys():
        if i > int(chutes_ladders.get(i)):
            print(i, "Shoot")
        elif i < int(chutes_ladders.get(i)):
            print(i, "Ladder")
    else:
        pass

question = input(" Go Further?: Y or N : ")
dice = 0
position = 1
board = []

while question.upper() == 'Y':
    # print(f'your number is {randint(1, 6)}')

    dice += randint(1, 6)
    print("Your dice is", dice)
    position += dice

    if position in chutes_ladders:
        position = chutes_ladders.get(position)
    else:
        pass

        # chutes_ladders = dict((y, x) for x, y in chutes_ladders.items())


        # if position == 4:
        #   print(position)
        #  position = 7
        # elif position == 8:
        #   print(position)
        #  position = 15
    print("Your position is ", position)

    ques = input('Do you want to roll again !!')
    dice = 0

    if position >= 36:
        print("You went over 36 and have won!!!")
        break
else:
    print('Thank you For Playing')
