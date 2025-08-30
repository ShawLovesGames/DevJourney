# ---Print the sum of digits of a number without converting it to a string---

n = int(input("Enter a number: "))
sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n = n // 10
print("The sum of the digits is: " + str(sum))