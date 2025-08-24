# ---Ask for a number and check if it’s divisible by both 3 and 5---

num2 = int(input("Enter a number: "))
if num2 % 3 == 0 and num2 % 5 == 0:
    print("The number is divisible by both 3 and 5.")
elif num2 % 3 == 0:
    print("The number is divisible by only 3.")
elif num2 % 5 == 0:
    print("The number is divisible by only 5.")
else:
    print("The number is neither divisible by 3 nor 5.")