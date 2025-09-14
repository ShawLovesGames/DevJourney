# ---Without using multiplication (*), compute the product of all numbers in a list---

lst = [1, 2, 3, 4, 5]
product = 1

for i in lst:
    j = 0
    for k in range(i):
        j += product
    product = j

print(product)