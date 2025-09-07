# ---Nested if statements---

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 < num2:
    if num2 < num3: # if statement inside another if statement is valid.
        print("The third number is greatest.")
    else:
        print("The third number is not the greatest.")
else:
    print("The second number is not greater than the first number.")