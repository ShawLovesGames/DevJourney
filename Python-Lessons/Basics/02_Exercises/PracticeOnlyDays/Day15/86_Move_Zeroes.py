# ---Write a program to move all zeros to the end of a list without changing the order of non-zero elements---

lst = [0, 0, 1, 2, 0, 3, 0]

new_list = [i for i in lst if i != 0]
new_list.extend([0] * lst.count(0))

print(new_list)