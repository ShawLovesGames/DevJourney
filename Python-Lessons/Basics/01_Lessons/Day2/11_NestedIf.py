# ---Nested if statements---

num1 = 1
num2 = 2
num3 = 3
if num1 < num2:
    if num2 < num3: # if statement inside another if statement is valid.
        print("Num3 is greatest.")
    else:
        print("Num3 is not the greatest.")
else:
    print("Num2 is not greater than num1")