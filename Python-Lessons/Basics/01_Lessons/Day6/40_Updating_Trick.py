# ---Trick to Update a Tuple---

'''
    As tuples are immutable we cannot directly change it's values.
    We can convert the tuple to list using the list() constructor and update the values.
    We can change the list back to a tuple using the tuple() constructor.
'''

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
my_list = list(my_tuple)
my_list.insert(0, 0)
my_tuple = tuple(my_list)

print(my_tuple)

'''
    With this trick we can perform almost all operations on tuples.
    Note :- We can add tuples to tuples.
'''

my_other_tuple = (11, 12, 13, 14, 15)
my_tuple += my_other_tuple
print(my_tuple)

# ---We can use del keyword to delete a tuple completely---

del my_tuple
del my_other_tuple
del my_list