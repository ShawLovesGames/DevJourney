# ---Write a program to count how many distinct elements are in a tuple---

tup = (1, 2, 3, 4, 5, 1, 3, 5)
count = 0
elements = ""

for i in tup:
    if str(i) not in elements:
        elements += str(i)
        count += 1

print(f"The total length of the tuple is {len(tup)} but the distinct elements are {count}")