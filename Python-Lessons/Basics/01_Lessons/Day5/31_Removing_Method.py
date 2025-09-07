# ---Methods Used to Remove Items from a List---


# ---Remove Method---
"""
    The remove() method removes the first occurrence specified item from the list.
    remove() modifies the original list in-place.
    It searches for the first element that is equal to the given value and removes it. 
    All subsequent elements are shifted to the left to fill the gap.
    It does not remove items by index.
"""
Food = ["Biryani", "Pulao", "Fried Rice"]
Food.remove("Pulao") # Removing the item "Pulao".
print(Food)


# ---Pop Method---
"""
    pop() method is used to remove an item at the specified index.
    The pop() method is a built-in function for lists that removes and returns an element from a specific position in the list. 
    If no index is specified, it removes and returns the last element.
    If we use pop() without any arguments the last item will be removed and returned.
    It takes either no arguments or max 1 argument.
"""
print(Food.pop(1)) # Removing the item at index 1 and printing it.


# ---Del Keyword---
"""
    We can use del keyword to delete the specified index.
    Its behavior changes depending on what you use it on, making it a versatile tool for cleanup and management.
    We can also use del keyword to delete the entire list.
"""
My_List = ["Python", "JAVA", "C", "MySQL", "HTML", "CSS", "JavaScript", "PHP"]
del My_List[4] # Deletes the item "HTML".
print(My_List)
del My_List[1:3] # Deleted the items "JAVA", "C".
print(My_List) 
del My_List # Deletes the entire list.


# ---Clear Method---
"""
    clear() method is used to empty a list, the list still remains but there are no items in the list.
    clear() method works in-place, meaning it modifies the original object directly and does not create a new one.
    The clear() method returns None.
"""
Food.clear() # Empties the Food list.
print(Food) # Prints the empty list.