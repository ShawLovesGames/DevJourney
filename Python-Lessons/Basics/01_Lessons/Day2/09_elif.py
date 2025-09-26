# ---If-elif-else statements---

num1 = 25
num2 = 25
if num1 > num2: # Checking if the first number is greater.
    print(str(num1) + " is greater than " + str(num2) + ".")
elif num1 == num2: # Checking if both the numbers are equal.
    print("Both numbers are equal.") # This is the suite that will be executed because the condition is true.
else: # else keyword doesn't take a condition as it is supposed to be executed when all given conditions are false.
    print("The first number is not greater than the second and they are also not equal.")