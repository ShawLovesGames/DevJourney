# ---Take three numbers and find the largest using only if and elif (no logical operators)---

num3 = int(input("Enter the first number: "))
num4 = int(input("Enter the second number: "))
num5 = int(input("Enter the third number: "))
if num3 > num4:
    if num3 > num5:
        print(str(num3) + " is the greatest number.")
    elif num3 < num5:
        print(str(num5) + " is the greatest number.")
elif num4 > num3:
    if num4 > num5:
        print(str(num4) + " is the greater number.")
    elif num4 < num5:
        print(str(num5) + " is the greatest number.")
else:
    print("Any two of the three numbers is equal and hence greatest number cannot be determined.")