# ---WAP to count how many digits of a number are even or odd---

n = int(input("Enter the number: "))
even = 0
odd = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        even += 1
    else:
        odd += 1
    n //= 10
print("The number has ", even, " even numbers and ", odd, " odd numbers.")