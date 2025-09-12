# ---Accessing the Items in a Tuple Using Indexing---

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(my_tuple[1]) # Printing the item at index 1.

# ---Negative Indexing---

print(my_tuple[-1]) # Printing the last item using negative indexing.

# ---Slicing or Range of Indexes---

print(my_tuple[2:5]) # Note :- The last index (in this case - '5') is not included.
print(my_tuple[:4]) # Leaving out values in list slicing is same as string slicing.
print(my_tuple[-5:-2]) # Negative indexing works. -2 will not be included.