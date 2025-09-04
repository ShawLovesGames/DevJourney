# ---Print the following pattern for n = 4---
# 1
# 12
# 123
# 1234

n = int(input("Enter the number: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()