# ---Count how many digits are in a string---

s = input("Enter the string: ")
count = 0
for i in s:
    if i.isdigit():
        count += 1     
print(count)