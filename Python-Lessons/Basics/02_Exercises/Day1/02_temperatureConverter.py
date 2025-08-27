# ---Program to input the temperature in Celsius and convert it to Fahrenheit---

celsius = int(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32 # Formula to convert Celsius to Fahrenheit F = (C * 9/5) + 32
print("Temperature in Fahrenheit: " + str(fahrenheit))