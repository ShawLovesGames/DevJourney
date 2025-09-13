# ---Write a program to count how many distinct elements are in a tuple---

tup = (1, 2, 3, 4, 5, 1, 3, 5)
last = []
count = 0

for i in tup:
    if i not in last:
        last.append(i)
        count += 1

print(f"The total length of the tuple is {len(tup)} but the distinct elements are {count}")