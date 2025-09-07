# ---List Comprehension---

"""
    List comprehension is used to create a list based on another list with shorter syntax.
    We can filter the items using List comprehension.
    It is the pythonic alternative to using for loop with append.
"""
My_List = ["Python", "JAVA", "C", "MySQL", "HTML", "CSS", "JavaScript", "PHP"]
New_List = [x for x in My_List] # The for loop iterates over the old list and the items are append-ed to the new list.
print(New_List)
print(My_List) # The old list is not changed at all.


# ---Using a Conditional Statement---

New_List2 = [x for x in My_List if "H" in x] # The if statements filters the items and only the items that have "H" are append-ed.
print(New_List2)


# ---List Comprehension is Iterable---

New_List3 = [x for x in range(10)] # Integers from 0 to 9 are added as items in the list.
print(New_List3)


# ---Expressions in List Comprehension---

New_List4 = [x.upper() for x in "hello"] # We can modify the current items before adding it to the new list.
print(New_List4)

New_List5 = [x if x != 'e' else 'i' for x in "hello"] # We can use conditionals to modify the items before adding them to the list.
print(New_List5)

New_List6 = ["*" for x in My_List] # We can replace all items with a different value but keep the length of the new string same as the old string.
print(New_List6)