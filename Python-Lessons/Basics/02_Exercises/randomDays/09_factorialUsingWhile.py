# ---Print the factorial of a number using while loop---

n = int(input("Enter a number: "))
count = 1
factorial = 1
while count <= n:
    factorial = factorial * count
    count += 1
print(factorial)