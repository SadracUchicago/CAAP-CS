try:
    total = 0

    User_Input_List = input("What is your number list?: ")
    User_Input_List = [int(x) for x in User_Input_List.split(" ")]

    for i in User_Input_List:
        total += i
    print("The sum of the list is", total)
except ValueError:
    print("Incorrect input")

