# ---Tuples in Python---

'''
    Tuples, like lists, are used to store multiple items in a single variable
    A tuple is created using round brackets
'''

my_tuple = (1, 2, 3)
print(my_tuple)

'''
    Tuple items are indexed. The first item of the tuple will have index 0.
    Tuple items are ordered. The items have an defined order and that order will not change.
    Tuple items are immutable. We cannot change, add or remove items after the tuple has been created.
    Tuples can store items of different data type.
    Tuples allow duplicate value.
'''

new_tuple = ("Akshat", 3.14, 20, "Python", 3.14) # Tuple containing values of different data types and also a duplicate value.
print(new_tuple)
print(type(new_tuple)) # Tuples are objects of "tuple" data type.
print(len(new_tuple)) # Printing the length of the tuple by using len() function.

# ---Tuple Constructor---

# We can use the tuple() constructor to create tuples.
newest_tuple = tuple(("Hello", ",", "World"))
print(newest_tuple)