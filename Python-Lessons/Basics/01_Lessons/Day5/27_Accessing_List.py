# ---Accessing the Items in a List Using Indexing---

My_List = ["Python", "JAVA", "C", "MySQL", "HTML", "CSS", "JavaScript", "PHP"]
print(My_List[5]) # We can print the item at desired index..

# ---Negative Indexing---

print(My_List[-1]) # Python allows negative indexing for lists too.

# ---Slicing or Range of Indexes---

print(My_List[1:5]) # Note :- The last index (in this case - '5') is not included.
print(My_List[:3]) # Leaving out values in list slicing is same as string slicing.
print(My_List[-5:-2]) # Negative indexing works. -2 will not be included.