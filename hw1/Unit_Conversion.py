quantity, units = input("Enter amount with units: ").split()[:2]
conversion = eval(quantity)*{'inches': 2.54, 'centimeters': 0.393701}[units]

print(conversion)
