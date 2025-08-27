# ---Use a for loop and else to check if a number is prime---

num = int(input("Enter a number: "))
if num <= 1:
    print("Invalid number.")
for x in range(2, num):
    if num % x == 0:
        print("Not a prime number.")
        break
else:
    print("Prime number!")