# ---Write a loop that prints all elements of a tuple in reverse order (without slicing)---

my_tuple = (1, 2, 3, 4, 5, 6)
count = -1

for i in my_tuple:
    print(my_tuple[count], end=" ")
    count -= 1