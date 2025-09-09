# ---Replace all negative numbers in a list with 0---

lst = [3, -2, 7, -5, 8, -1]

for i in range(len(lst)):
    if lst[i] < 0:
        lst[i] = 0

print(lst)