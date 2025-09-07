# ---Membership Operators Usage in Lists---

My_List = ["Python", "JAVA", "C", "MySQL", "HTML", "CSS", "JavaScript", "PHP"]

if "Python" in My_List: # Using in operator to check if a certain item is in a list.
    print("I know python!")
else:
    print("I don't know python!")

if "Rust" not in My_List: # Using not in operator to check if a certain item is not in a list.
    print("I don't know rust!")
else:
    print("I know rust!")