# ---Print the sum of Numbers Divisible by 3 or 5---

limit = int(input("Enter the limit: "))
total = 0
for i in range(1, limit+1):
    if i % 3 == 0:
        total += i
    elif i % 5 == 0:
        total += i
print("The sum is", total)