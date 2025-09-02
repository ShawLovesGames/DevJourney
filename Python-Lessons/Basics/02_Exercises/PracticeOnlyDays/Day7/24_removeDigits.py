# ---WAP to remove all numbers from a string---

s = input("Enter the string: ")
for i in s:
    if i.isalpha():
        print(i, end="")
    else:
        continue