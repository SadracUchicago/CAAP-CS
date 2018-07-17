### lots of help from stackexchange to be completely honest; I did not understand this problem

Minimum = eval(input("How much is your change?: "))


def main(remainder):

#starting value defined by value of Minimum variable

    change = ()
#empty tuple
    for i in [.25, .10, .05, .01]:
#goes through greatest values first
        num = int(remainder/i)
        change = change + (i,) * num
        remainder = remainder-(i * num)
#remainder is the value that still persists after every iteration of i and its operations
    return change


print("The number of coins needed to formulate this change: ", len(main(Minimum)))
print("The coins needed are", main(Minimum))
