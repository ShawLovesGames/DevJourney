# ---Print the first N terms of the Fibonacci series---

n = int(input("Enter the number of terms: "))
first = 0
second = 1
if n >= 1:
    print(first)
if n >= 2:
    print(second)
for i in range(2, n):
    next_term = first + second
    print(next_term)
    first = second
    second = next_term