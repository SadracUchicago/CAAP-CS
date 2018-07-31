age = int(input("What is your age?: "))
citizenship = int(input("Years of citizenship?: "))
if age >= 35 and citizenship >= 9:
    print("You are eligible to serve as a US Senator.")
    if age >= 25 and citizenship >= 7:
        print("You are eligible to serve a a US Representative")
else:
    print("You are neither eligible to serve as Senator nor Representative.")
