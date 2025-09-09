# ---Merge two lists into a single list without .extend()---

list1 = [1, 2, 3]
list2 = [4, 5, 6]

for i in list2:
    list1.append(i)

print(list1)