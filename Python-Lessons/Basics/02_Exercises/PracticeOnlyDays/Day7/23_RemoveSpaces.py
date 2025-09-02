# ---WAP to remove all spaces from a string---

s = input("Enter a sentence: ")
for i in s:
    if i == " ":
        continue
    else:
        print(i, end="")