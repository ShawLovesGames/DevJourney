# Program to input two numbers and performing addition, subtraction, multiplication and division operations on them.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2 # Addition
diff = num1 - num2 # Subtraction
prod = num1 * num2 # Multiplication
quot = num1 / num2 # Division
print("Sum: " + str(sum))
print("Difference: " + str(diff))
print("Product: " + str(prod))
print("Quotient: " + str(quot))


# Program to input the temperature in Celsius and convert it to Fahrenheit.
celsius = int(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32 # Formula to convert Celsius to Fahrenheit F = (C * 9/5) + 32
print("Temperature in Fahrenheit: " + str(fahrenheit))


# Program to format the name of the user.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Hello " + first_name + " " + last_name + "!") # Concatenation of strings using + operator


# Program to find the square and cube of a number.
num3 = int(input("Enter a number: "))
square = num3 ** 2 # Square of a number using ** operator
cube = num3 ** 3 # Cube of a number using ** operator
print("Square of the number: " + str(square))
print("Cube of the number: " + str(cube))


# Program to convert distance from kilometers to miles.
kilometers = float(input("Enter distance in kilometers: "))
miles = kilometers * 0.621371 # Formula to convert kilometers to miles: miles = kilometers * 0.621371
print("Distance in miles: " + str(miles))