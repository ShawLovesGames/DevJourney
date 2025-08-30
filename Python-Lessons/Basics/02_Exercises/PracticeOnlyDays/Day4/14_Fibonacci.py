# ---Print the first N terms of the Fibonacci series---

n = int(input("Enter the number of terms: "))
first = 0
second = 1
print(first)
print(second)
n -= 2
x = False
while x == False:
    next_term = first + second
    print(next_term)
    n -= 1
    first = second
    second = next_term
    if n == 0:
        x = True