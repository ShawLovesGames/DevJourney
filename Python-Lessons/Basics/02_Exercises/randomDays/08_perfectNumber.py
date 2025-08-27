# ---Write a program to check if a number is a perfect number---

n = int(input("Enter the number: "))
check = 0
for i in range(1, n):
    if n % i == 0:
        check += i
    else:
        continue
if check == n:
    print("It is a perfect number.")
else:
    print("It is not a perfect number.")