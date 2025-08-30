# ---Print the squares or cubes of numbers from 1 to N based on user needs---

n = int(input("Enter the limit: "))
operation = int(input("Enter 1 for square or 2 for cube: "))
for i in range(1, n+1):
    if operation == 1:
        square = 0
        square = i*i
        print(square)
    elif operation == 2:
        cube = 0
        cube = i*i*i
        print(cube)
    else:
        print("Invalid choice!")
        break