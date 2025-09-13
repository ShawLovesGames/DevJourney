# ---Given a tuple of numbers, create a new tuple containing only the prime numbers---

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
lst = []

for i in tup:
    if i < 2:
        continue
    isPrime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        lst.append(i)
            
new_tup = tuple(lst)

print(new_tup)