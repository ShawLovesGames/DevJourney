# ---Print the Fibonacci sequence up to a given limit---

n = int(input("Enter the limit: "))
a, b = 0, 1
if n > 0:
    print(a, end=" ")
while b < n:
    print(b, end=" ")
    c = a + b
    a = b
    b = c