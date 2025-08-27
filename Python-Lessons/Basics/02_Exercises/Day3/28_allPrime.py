# ---Print all prime numbers between 1 and 100 using loops---

for num in range(2, 100):
    if num == 2:
        continue
    for x in range(2, num-1):
        if num % x == 0:
            break
    else:
        print(num)