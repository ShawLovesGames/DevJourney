# ---Swap the first and last elements of a tuple (tuples are immutable)---

tup = (1, 2, 3, 4, 5)

lst = list(tup)

lst[0], lst[-1] = lst[-1], lst[0]

tup = tuple(lst)

print(tup)