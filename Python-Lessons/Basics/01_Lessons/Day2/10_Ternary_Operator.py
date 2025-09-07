# ---Ternary Operators in python (also called Condtional Expressions)---

num1 = 1
num2 = 2
num3 = 3
if num1 < num2: print("The first number is smaller.") # Short hand if
print("A") if num3 > num2 else print("B") # Short hand if...else || Output will be A.
print("A") if num1 > num2 else print("=") if num1 == num2 else print("B") # One line if else statement with 3 conditions. Completely valid.