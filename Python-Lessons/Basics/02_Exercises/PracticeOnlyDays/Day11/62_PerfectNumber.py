# ---Check if a number is perfect---

n = int(input("Enter a number: "))
check = 0
for i in range(1, n//2 + 1): # Note :- I have done this question before but I made it inefficient by looping till n.
    if n % i == 0:
        check += i
if check == n: print("It is a perfect number.")
else: print("It is not a perfect number")