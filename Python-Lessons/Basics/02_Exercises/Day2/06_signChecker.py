# ---Take a number from the user, check if it’s positive, negative, or zero---

num = int(input("Enter the number: "))
if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")