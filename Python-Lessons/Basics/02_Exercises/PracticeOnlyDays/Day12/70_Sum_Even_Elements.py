# ---Take a list of integers and print the sum of all even numbers---

lst = [1, 2, 3, 4, 5, 6, 7, 8]
sum = 0

for i in lst:
    if i % 2 == 0:
        sum += i
        
print(sum)