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

# ---Logical Operators use in conditional statements---

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num3 > num1 and num3 > num2: # Using and operator to check if num1 is greater than two numbers in one statement.
    print("The third number is the greatest number.")
elif num2 > num1 and num2 > num3:
    print("The second number is the greatest number.")
else:
    print("The third number is the greatest number.")

# ---Identity Operators use in conditional statement---

value = None
if value is None: # Note "is" identity operator can be used as "==" operator when dealing with None values
    print("No value yet.")
else:
    print("Value is present.")