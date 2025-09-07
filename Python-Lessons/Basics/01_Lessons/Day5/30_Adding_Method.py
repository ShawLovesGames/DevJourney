# ---Method Used to Add Items to Lists---


# ---Insert Method---
"""
    The insert() method can be used to insert new items in a list at any index.
    The new element is inserted before the item currently at the specified index.
    All elements from that index onward are shifted to the right (their indices increase by 1)
"""
Food = ["Biryani", "Pulao", "Fried Rice"]
Food.insert(2, "Paneer") # Inserting the item "Paneer" at index 2 or position 3.
print(Food)


# ---Append Method---
"""
    The append() method can be used to insert items at the end of the list.
    append() modifies the original list in-place. This means it doesn't create a new list; it changes the existing one. 
    It also returns None, so you should never assign the result of append() to a variable.
    It only takes one single argument. We use extend() to add multiple items.
"""
Food.append("Chickpea Coconut") 
print(Food) # Prints updated list with "Chickpea Coconut" string as the last item.


# ---Extend Method---
"""
    The extend() method is used to append elements of any other iterable to the current list.
    extend() iterates over the given iterable and appends each element one by one to the end of the original list.
    It modifies the list in-place and returns None.
    The extend() method can append any iterable object (tuples, sets, dictionaries etc.).
"""
Snacks = ["Burger", "Sandwich", "Momos"]
Food.extend(Snacks) # Extending the Food list with the Snack list.
print(Food)