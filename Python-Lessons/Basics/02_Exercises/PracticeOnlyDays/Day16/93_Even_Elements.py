# ---Given a tuple of integers, print a new tuple containing only the even numbers---

tup = (1, 2, 3, 4, 5, 6, 7, 8)

new_tup = tuple(i for i in tup if i % 2 == 0)

print(new_tup)