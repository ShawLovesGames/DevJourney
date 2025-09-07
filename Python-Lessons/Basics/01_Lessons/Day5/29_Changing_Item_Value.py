# ---Changing the Value of Items in a List---

My_List = ["Python", "JAVA", "C", "MySQL", "HTML", "CSS", "JavaScript", "PHP"]
My_List[7] = "Go" # We can refer to the index number to change any item in the list.
print(My_List) 

# Reminder :- Lists are mutable, strings are not.

# Changing the value in a range of indexes.
My_List2 = ["Akshat", "Shaw", 20, "Male", True, 3.14, True]
My_List2[4:6] = ["India", "Asia"] # We can change a range of items in a list by refering to the index and defining a new string.
print(My_List2)

# What if we add more items than we replace?
My_List3 = ["Biryani", "Pulao", "Fried Rice"]
My_List3[1:2] = ["Paneer", "Chickpea coconut"] # The new items are inserted at the referred index and the items after the index are shifted accordingly.
print(My_List3)
# Note :- The length of the list will increase based on insertions.

# What if we less more items than we replace?
My_List3[1:3] = ["Pulao"] # The items at the referred index will be removed anyway and "Pulao" will be added.
print(My_List3)
# Note :- The length of the list will decrease based on items removed.

#* Note :- There are many list methods that can we used to add or remove items without needing to replace other items.