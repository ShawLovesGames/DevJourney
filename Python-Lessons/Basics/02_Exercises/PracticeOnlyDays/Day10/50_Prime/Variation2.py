# ---Check if the sum of the digits of the number is prime---

n = int(input("Enter the number: "))
sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n //= 10
if sum < 2:
    print(f"The sum of the digits {sum} is not prime.")
else:
    is_prime = True
    for i in range(2, int(sum**0.5) + 1):
        if sum % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"The sum of the digits {sum} is prime.")
    else:
        print(f"The sum of the digits {sum} is not prime.")