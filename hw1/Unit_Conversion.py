print("This short program is designed to convert centimeters to inches or inches to centimeters. Whilst using it, "
      "please include the necessary notation.")

### short explanation of program
measurement, units = input("Enter amount with units: ").split()[:2]

### necessitates user input of both the numerical measurement and it's units

conversion = eval(measurement) * {"inches": 2.54, "centimeters": 0.393701}[units]
# the input, whether inches or centimeters will be designated its own operation
print(conversion)
