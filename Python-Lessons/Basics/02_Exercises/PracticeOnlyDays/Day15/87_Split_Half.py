# ---Write a program to split a list into two halves and print both halves---

lst = [1, 2, 3, 4, 5, 6]
first_half = []
second_half = []

count = len(lst) // 2

for i in range(len(lst)):
    if i < count:
        first_half.append(lst[i])
    else:
        second_half.append(lst[i])

print(first_half)
print(second_half)