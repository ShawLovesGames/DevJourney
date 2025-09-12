# ---Looping Through A Tuple---

# We can loop through a tuple using a For loop.

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for i in my_tuple:
    print(i, end=" ")
print()

# We can loop through a tuple by referring to the index numbers by using range() and len().

for i in range(len(my_tuple)):
    print(my_tuple[i], end=" ")
print()

# We can use the while loop to loop through a tuple.

x = 0
while x < len(my_tuple):
    print(my_tuple[x], end=" ")
    x += 1