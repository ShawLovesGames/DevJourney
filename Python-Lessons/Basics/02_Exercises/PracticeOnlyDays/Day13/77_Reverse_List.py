# ---Reverse a list using a loop (not .reverse() or slicing)---

lst = [1, 2, 3, 4, 5]
reversed_lst = []

for i in lst:
    reversed_lst = [i] + reversed_lst

print(reversed_lst)