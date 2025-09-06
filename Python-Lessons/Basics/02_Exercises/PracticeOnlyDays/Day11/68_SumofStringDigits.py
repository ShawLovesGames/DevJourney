# ---Sum of Digits in a String---

s = input("Enter the string: ")
digits = ""
for i in s:
    if i.isdigit():
        digits += i
temp = int(digits)
sum = 0
while temp > 0:
    Last_digit = temp % 10
    sum += Last_digit
    temp //= 10
print(sum)