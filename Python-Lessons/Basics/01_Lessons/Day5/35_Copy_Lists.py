# ---Copy Method---

# We use the copy() method to copy a list to another list because simply using an assignment operator only stores the reference.
My_List = [1, 2, 3, 4, 5]
New_List = My_List.copy() # Copies the elements of My_List and adds them to the New_List.
print(New_List)

# ---List Method---

# Alternatively we can use the list() method to copy the elements of another list to a new list.
New_List2 = list(My_List) # Using the list() method ensures the list is stored instead of the refernce.
print(New_List2)

# ---Using Slicing---

# We can also copy a list from an old list using slicing.
New_List3 = My_List[:] # Slicing from index 0 to the last index.
print(New_List3)