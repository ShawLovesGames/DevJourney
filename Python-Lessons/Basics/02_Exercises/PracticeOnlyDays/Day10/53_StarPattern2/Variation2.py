# ---Print odd numbers only---
# 1
# 13
# 135
# 1357

n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        odd = 2 * j - 1
        print(odd, end="")
    print()