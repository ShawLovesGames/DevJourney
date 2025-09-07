# ---Sort Method---

# The sort() method is used to sort a list alphanumerically. It is ascending by default.
My_List = ["Python", "JAVA", "C", "MySQL", "HTML", "CSS", "JavaScript", "PHP"]
My_List.sort() # Sorts the list alphabetically.
print(My_List)

Num_List = [32, 12, 72, 52, 102]
Num_List.sort() # Sorts the list numerically from smallest to greatest.
print(Num_List)

# ---Reverse Argument---

# We use the reverse keyword argument to set the sort to descending.
My_List.sort(reverse = True) # Sorts the list alphabetically but descending.
print(My_List)

Num_List.sort(reverse = True) # Sorts the list numerically from greatest to smallest.
print(Num_List)

# ---Key keyword---

# The key keyword is a parameter used to customize built in functions like sorting.
My_List2 = ["aaa", "BBB", "ccc", "DDD"]
My_List2.sort() # Sorts the list in unexpected format due to case.
print(My_List2)

My_List2.sort(key = str.lower) # Using key keyword to pass an argument to modify our outcome.
print(My_List2)

# We can customize the sort method using our own functions and key keyword. Which I will learn later when I study functions.

# ---Reverse Method---

# We can use reverse method to reverse a list's item's order.
My_List2.reverse() # Simply reverses the list.
print(My_List2)