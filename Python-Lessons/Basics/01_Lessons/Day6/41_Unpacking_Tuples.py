# ---Unpacking A Tuple---

'''
    When we normally create tuple, it is called "Packing" a tuple.
    In python we can extract and assign the values from a tuple into variables.
    This is called unpacking.
'''

my_tuple = (1, 2, 3) # Packing a tuple.
(one, two, three) = my_tuple # Unpacking a tuple into variables.
print(one, two, three) # Printing the extracted values.

'''
    If the number of variables doesn't match the number of values,
    We can add an "*" to the variable name and the extra values will be assigned to the variable as a list.
'''

my_other_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
(un, deux, trois, quatre, *cinq) = my_other_tuple # The first 4 values will be assigned to the first 4 variables and rest to the fifth variable.
print(un, deux, trois, quatre, cinq) # Printing the extracted values.

'''
    When the asterisk is added to any variable other than the last,
    Python will assign values to the variable to match the exact number of variables.
'''

(uno, dos, *tres, cuatro, cinco) = my_other_tuple # The first 2 values will be assigned to the first 2 variables and the last 2 values will be assigned to the last 2 variables.
print(uno, dos, tres, cuatro, cinco) # Printing the extracted values.