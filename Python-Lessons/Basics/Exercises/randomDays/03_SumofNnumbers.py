# ---Print the sum of first N numbers---

n = int(input("Enter the number of elements for sum: "))
sum = 0
for i in range(1, n+1):
    sum = sum + i
print(sum)