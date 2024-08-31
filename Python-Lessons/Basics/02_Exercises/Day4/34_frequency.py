# ---Find frequency of each character in a string---

s = input("Enter the string: ")
temp = ""
for i in s:
    if i not in temp:
        print(f"{i} occurred {s.count(i)} times.")
        temp += i