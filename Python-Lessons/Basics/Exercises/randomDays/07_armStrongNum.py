# ---WAP to check if a given number is an armstrong number---

n = int(input("Enter a positive number: "))
temp = orig = n
count = 0
total = 0
while n > 0:
    n = n // 10
    count += 1
while temp > 0:
    digit = temp % 10
    total += digit**count
    temp //= 10
if total == orig:
    print("The number is an armstrong number.")
else:
    print("The number is not an armstrong number.")