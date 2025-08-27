# ---Use a for loop to print the following multiplication tables (1 to 5) side by side---
# 1x1=1   2x1=2   3x1=3   4x1=4   5x1=5
# 1x2=2   2x2=4   3x2=6   4x2=8   5x2=10

rows = int(input("Enter the number of rows: "))
tables = int(input("Enter the number of tables."))
for x in range(1, rows+1):
    for y in range(1, tables+1):
        print(f"{y} x {x} = {y*x}", end="   ")
    print()