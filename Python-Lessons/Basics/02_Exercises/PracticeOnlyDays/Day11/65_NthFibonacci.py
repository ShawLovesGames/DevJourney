# ---Print the Nth Fibonacci number---

n = int(input("Enter the term: "))
a = 0
b = 1
c = 0
count = 1
if n == 1:
    print(0)
else:
    while count < n:
        if c == 0:
            count += 1
            c += 1
            continue
        else:
            c = a + b
            a = b
            b = c
            count += 1
print(c)