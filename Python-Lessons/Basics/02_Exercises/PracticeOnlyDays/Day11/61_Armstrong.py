# ---Check if a number is an Armstrong number---

n = int(input("Enter the number: "))
length = len(str(n))
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit ** length
    temp //= 10
if sum == n: print("The number is an armstrong number.")
else: print("The number is not an armstrong number.")