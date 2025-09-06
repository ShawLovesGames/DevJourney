# ---Pyramid of Stars (center aligned)---

count = 1
n = int(input("Enter the number of rows: "))
for i in range(n, 0, -1):
    print(" "*i + "*"*count)
    count += 2