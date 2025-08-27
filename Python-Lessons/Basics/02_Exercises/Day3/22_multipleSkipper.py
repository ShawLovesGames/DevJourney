# ---Print all numbers from 1 to 50, but skip multiples of 5 using continue---

for x in range(1, 50):
    if x % 5 == 0:
        continue
    else:
        print(x)