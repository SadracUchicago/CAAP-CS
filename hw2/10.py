year = int(input("What year's easter are you interested in?: "))
a = year % 19
b = year % 4
c = year % 7
d = (19 * a + 24) % 30
e = ((2 * b) + (4 * c) + (6 * d) + 5) % 7

Easter = 22 + d + e

if Easter <= 31:
    if year == 1954 or year == 1981 or year == 2049 or year == 2076:
        Easter -= 7
        print("March", Easter)
    else:
        print("March", Easter)
elif Easter > 31:
    if year == 1954 == 1981 == 2049 == 2076:
        Easter -= 7
        print("April", Easter - 31)
    else:
        print("April", Easter - 31)
