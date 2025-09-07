# ---Lists in Python---

'''
    Lists are used to store multiple items in a single variable.
    A list is created using square brackets.
'''

My_List = ["Python", "JAVA", "C", "MySQL", "HTML", "CSS", "JavaScript", "PHP"] # Creating a list of some programming languages and front-end development technologies.
print(My_List) # Printing the list.

'''
    List items are indexed. The first item of the list will have the index 0.
    List items are ordered. The items have the defined order and will not change. New items will be added at the end of the list.
    List items are mutable. The items in the list can be changed, added or removed even after it has been created.
    Lists can store multiple data types. A string, an integer, a boolean value or a decimal number can all be stored in one list.
    Lists allow duplicate items.
'''

My_List2 = ["Akshat", "Shaw", 20, "Male", True, 3.14, True] # List containing values of different data types and also a duplicate value.
print(My_List2)

print(type(My_List), type(My_List2)) # Lists are objects of "list" data type.
print(len(My_List), len(My_List2)) # We can use len() to print the number of items in a list.

# ---List Constructor---

# We can use the list constructor to create a list.
My_List3 = list(("Biryani", "Pulao", "Fried Rice"))
print(My_List3)