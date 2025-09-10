# ---Print the second largest element in a list (without sort() or max())---

lst = [5, 1, 9, 3, 7]
largest = lst[0]
second_largest = 0

for i in lst:
    if i > largest:
        second_largest = largest
        largest = i
    elif i < largest and i > second_largest:
        second_largest = i
    
print(second_largest)