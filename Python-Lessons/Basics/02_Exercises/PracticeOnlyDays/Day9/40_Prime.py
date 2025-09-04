# ---Check if a number is prime---

n = int(input("Enter the number: "))
prime = False
for i in range(2, n):
    if n % i == 0:
        break
else:
    prime = True
if prime:
    print("The number is prime.")
else:
    print("The number is not prime.")