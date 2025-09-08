# ---Given a list with duplicates, create a new list with unique elements---

lst = ["AA", "AA", "BB", 1, 1, 2]
new_list = []

for i in lst:
    if i not in new_list:
        new_list.append(i)

print(new_list)