# ---Right-Aligned Triangle (n rows, * aligned to the right)---

n = int(input("Enter the number of rows: "))

for i in range(n, 0, -1):
    spaces = i - 1
    stars = n - i + 1
    print(" "*spaces,"*"*stars)