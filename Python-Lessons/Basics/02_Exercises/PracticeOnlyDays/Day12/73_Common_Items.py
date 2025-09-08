# ---Given two lists, print the elements common to both lists---

list1 = [0, 1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9, 0]

common = [x for x in list1 if x in list2]

print(common)