# ---Looping Through a List---

My_List = ["Python", "JAVA", "C", "MySQL", "HTML", "CSS", "JavaScript", "PHP"]

# We can print the items of a list using a for loop.
for i in My_List:
    print(i, end=" ") # Printing the items one by one.

print()

# We can print the items of a list by referring their index number using range() and len() functions.
for i in range(len(My_List)):
    print(My_List[i], end=" ")

print()

# We can also use a while loop to print the items of a list.
i = 0
while i < len(My_List):
    print(My_List[i], end=" ")
    i = i + 1