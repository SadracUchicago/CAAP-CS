Fahrenheit = eval(input("What is the temperature in Fahrenheit?: "))
### User input decides the initial f value
Celsius = ((Fahrenheit - 32) * 5) / 9
###This computes the output via the conversion formula

print("The temperature in Celsius is", Celsius)
for i in range(0, 5):
    print(Celsius)

### loops goes over print 5 times before ending
