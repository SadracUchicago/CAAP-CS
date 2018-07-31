Credits = int(input("How many credits?: "))

if Credits in range(0, 7):
    print("The student is a freshman.")
elif Credits in range(7, 16):
    print("The student is a sophomore.")
elif Credits in range(16, 26):
    print("The student is a junior")
elif Credits > 26:
    print("The student is a senior")
else:
    print("Improper input")
