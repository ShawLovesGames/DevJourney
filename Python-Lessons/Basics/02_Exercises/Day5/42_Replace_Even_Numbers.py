# ---Replace all even numbers in a list with 0---

nums = [1, 2, 3, 4, 5, 6]
new_list = []

for i in nums:
    if i % 2 == 0:
        new_list.append(0)
    else:
        new_list.append(i)

print(new_list)