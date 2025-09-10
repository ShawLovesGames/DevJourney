# ---Remove all occurrences of a given element from a list without .remove()---

lst = [1, 2, 3, 2, 4, 2]
print(lst)
target = int(input("Enter the element to remove: "))

lst = [i for i in lst if i != target]

print(lst)