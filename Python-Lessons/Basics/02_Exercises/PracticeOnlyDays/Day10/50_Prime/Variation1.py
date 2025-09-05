# ---Count how many prime numbers are between 1 and n---

n = int(input("Enter the limit: "))
count = 0
if n < 2:
    print("Invalid limit")
else:
    for num in range(2, n):
        isprime = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                isprime = False
                break
        if isprime:
            count += 1
print(f"There are {count} prime numbers between 1 and {n}")