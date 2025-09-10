# ---Count how many times a given element appears in a list (without .count())---

lst = ["Python", "C", "Python", "JAVA"]
target = "Python"
count = 0

for i in lst:
    if i == target:
        count += 1
    
print(count)