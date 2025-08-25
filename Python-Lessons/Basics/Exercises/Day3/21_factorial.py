# ---Write a program that asks for a number and prints its factorial---

num = int(input("Enter the number: "))
factorial = 1
for x in range(1, num+1):
    factorial = factorial * x
print(factorial)