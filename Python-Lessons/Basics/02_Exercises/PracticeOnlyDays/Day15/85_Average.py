# ---Given a list of integers, create a new list with all numbers greater than the average of the list---

lst = [75, 80, 85, 90, 95, 100]
sum = 0
index = 0

while index < len(lst):
    sum += lst[index]
    index += 1

average = sum / len(lst)

new_list = [i for i in lst if i > average]

print(new_list)