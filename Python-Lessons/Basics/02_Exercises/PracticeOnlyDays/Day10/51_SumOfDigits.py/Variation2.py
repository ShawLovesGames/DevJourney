# ---Sum digits until the sum is a single digit (digital root)---

n = int(input("Enter the number: "))
while n >= 10:
    digit_sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        temp //= 10
    n = digit_sum
print(n)