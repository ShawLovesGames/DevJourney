n = int(input("Enter a number: "))
for i in range(1, n + 1):
    row = ""
    for j in range(1, i + 1):
        row = row + str(j)
    print(row)