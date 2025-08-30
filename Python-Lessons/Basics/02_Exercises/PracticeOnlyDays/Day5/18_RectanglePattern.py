# ---Print a square pattern of size 5 with hollow inside---
# *****
# *   *
# *   *
# *   *
# *****

size = int(input("Enter the size of the sides: "))

for i in range(1, size + 1):
    for j in range(1, size + 1):
        if i == 1 or i == size or j == 1 or j == size:
            print("*", end="")
        else:
            print(" ", end="")
    print()