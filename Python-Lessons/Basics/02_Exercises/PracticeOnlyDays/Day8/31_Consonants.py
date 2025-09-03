# ---Count consonants in a string---

s = input("Enter the string: ")
count = 0
for i in s:
    if i.isalpha() and i not in "aeiouAEIOU":
        count += 1
print(count)