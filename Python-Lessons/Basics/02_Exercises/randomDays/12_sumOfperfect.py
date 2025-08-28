# ---Find the sum of all perfect numbers between 1 and N---

n = int(input("Enter the number of perfect numbers: "))
total = 0
for i in range(1, n+1):
    check = 0
    for j in range(1, i):
        if i % j == 0:
            check += j
    if check == i:
        total += i
print(total)