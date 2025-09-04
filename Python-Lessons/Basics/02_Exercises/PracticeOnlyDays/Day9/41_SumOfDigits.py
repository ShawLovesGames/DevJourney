# ---WAP to print the Sum of digits of a number---

n = int(input("Enter the number: "))
temp = n
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit
    temp //= 10
print(f"The sum of the digits is: {sum}")