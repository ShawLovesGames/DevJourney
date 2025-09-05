# ---Reverse numbers---
# 4
# 43
# 432
# 4321

n = int(input("Enter the number of rows: "))
for i in range(n, 0, -1):
    for j in range(n, i-1, -1):
        print(j, end="")
    print()