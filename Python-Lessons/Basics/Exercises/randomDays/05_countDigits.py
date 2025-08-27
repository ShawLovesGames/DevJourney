# ---WAP to count how many digits are in a given number without converting it to a string---

n = int(input("Enter the number: "))
count = 0
while n > 0:
    n = n // 10
    count += 1
print("The number of digits is: " + str(count))