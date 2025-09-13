# ---Write a program to move all zeros to the end of a list without changing the order of non-zero elements---

lst = [0, 0, 1, 2, 0, 3, 0]

for i in lst:
    if i == 0:
        lst.append(0)
        lst.remove(0)
    
print(lst)