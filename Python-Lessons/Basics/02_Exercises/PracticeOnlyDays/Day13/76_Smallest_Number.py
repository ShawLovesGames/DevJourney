# ---Find the smallest number in a list without using min()---

lst = [12, 3, 45, 2, 19]
current = lst[0]

for i in lst:
    if i < current:
        current = i
    
print(current)