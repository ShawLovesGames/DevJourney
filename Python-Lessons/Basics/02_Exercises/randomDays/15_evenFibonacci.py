# ---Print the Fibonacci numbers that are even and less than 1000---

first = 0
second = 1
print(first)
print(second)
x = False
while x == False:
    next_term = first + second
    if next_term >= 1000:
        x = True
    elif next_term % 2 == 0:
        print(next_term)
        first = second
        second = next_term
    else:
        first = second
        second = next_term
        continue