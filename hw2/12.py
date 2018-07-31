import datetime
time = datetime.datetime.now()

date = input("What is the date [input in format d/m/yyyy?]: ")

convert = date.split('/')
for i in str((convert[0])):
    if len(i) > 2:
        print("Too many digits. Invalid Date.")
    elif len(i) < 1:
        print("Too few digits. Invalid Date.")
    else:
        pass

if int(convert[0]) < 0 or int(convert[0]) > 12:
    print("That is an invalid year.")


for i in str((convert[0])):
    if len(i) > 2:
        print("Too many digits. Invalid Date.")
    elif len(i) < 1:
        print("Too few digits. Invalid Date.")
    else:
        pass

if '31' in str(convert):
    if str(convert[0]) == '4' or str(convert[0]) == '6' or str(convert[0]) == '9' or str(convert[0]) == '11':
        print("that is an invalid date.")
elif '30' in str(convert[1]):
    if str(convert[0]) == '1' or str(convert[0]) == '3' or str(convert[0]) == '5' or str(convert[0]) == '7' or str(convert[0]) == '8' or str(convert[0]) == '10' or str(convert[0]) == '12':
        print("that is an invalid date")
elif '29' in str(convert[1]) or '28' in str(convert[1]):
    if '2' not in str(convert[0]):
        print("That is an invalid date")
elif int(convert[1]) < 0:
    print("That is an invalid year.")
elif int(convert[1]) > 31:
    print("That is not a valid year")
else:
    print("valid year")




