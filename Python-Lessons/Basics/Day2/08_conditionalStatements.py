# Condtional statements lets my code make decisions based on whether something is true or false.
# In python, indentation is used to define the scope of a keyword like if. Unlike C that uses curly brackets {}.

# ---If-else statements---
num1 = 15 # Initializing two variables with values.
num2 = 20
if num1 > num2: # Using if keyword to check if a given condition is true.
    print(str(num1) + " is greater.") # If the statement is true the suite (block of code) under the if statement is run. 
else: # Using else keyword to run another suite in case the given condition is false.
    print(str(num2) + " is greater.")

# ---If-elif-else statements---
num3 = 25
num4 = 25
if num3 > num4: # Checking if the first number is greater.
    print(str(num3) + " is greater than " + str(num4) + ".")
elif num3 == num4: # Checking if both the numbers are equal.
    print("Both numbers are equal.") # This is the suite that will be executed because the condition is true.
else: # else keyword doesn't take a condition as it is supposed to be executed when all given conditions are false.
    print("The first number is not greater than the second and they are also not equal.")

# ---Ternary Operators in python (also called Condtional Expressions)---
if num1 < num2: print("The first number is smaller.") # Short hand if

print("A") if num3 > num2 else print("B") # Short hand if...else || Output will be A.

print("A") if num1 > num2 else print("=") if num1 == num2 else print("B") # One line if else statement with 3 conditions. Completely valid.

# ---Nested if statements---
if num1 < num2:
    if num2 < num3: # if statement inside another if statement is valid.
        print("Num3 is greatest.")
    else:
        print("Num3 is not the greatest.")
else:
    print("Num2 is not greater than num1")

# ---Membership operators use in conditional statements---
name = "Akshat"
if 'A' in name: # Using membership operator to check if a given letter is present in a string.
    print("Letter A is in the string Akshat.")
    if 'Z' in name:
        print("The letter Z is in the string Akshat.")
    elif 'k' in name:
        print("The letter k is in the string Akshat.")
    else:
        print("The letter k is not in the string Akshat.")
else:
    print("Letter A is not in the string Akshat.")

# ---Logical Operators use in conditional statements--- # Note "is" membership operator can be used as "==" operator when dealing with None values
if num3 > num1 and num3 > num2: # Using and operator to check if num1 is greater than two numbers in one statement.
    print("Num3 is the greatest number.")
elif num2 > num1 and num2 > num3:
    print("Num2 is the greatest number.")
else:
    print("Num1 is the greatest number.")

value = None
if value is None: # Using is operator.
    print("No value yet.")
else:
    print("Value is present.")

# Pass statement can be used if we want an if statement which does not have a suite. Without the pass statement we would have an error.
if num1 <= num2:
    pass

# ---Chained comparisons---
if 0 < num1 < 20: # Chained comparison in one given statement. Valid.
    print("Num1 is greater than 0 but lesser than 20")
else:
    print("Num1 is either lesser than 0 or greater than 20")

#* ---TRUTHINESS---
surname = ""
if surname: # Empty strings, Zero and None are falsey.
    print("Truthy")
else:
    print("Falsey")

if not surname:  # Checks if surname is falsy.
    print("Surname not provided.")