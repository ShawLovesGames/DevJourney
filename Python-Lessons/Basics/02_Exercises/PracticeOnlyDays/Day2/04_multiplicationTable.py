# ---Print the multiplication table for a given number till a given limit---

n = int(input("Enter the number: "))
limit = int(input("Enter the limit: "))
i = 1
while i <= limit:
    print(f"{n} x {i} = {n*i}")
    i += 1