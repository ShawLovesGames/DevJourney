# ---Reverse the digits of a number using a while loop---

num = int(input("Enter a four digit number: "))
reversed_num = 0
while num > 0:
    i = num % 10
    reversed_num = reversed_num*10 + i
    num = num // 10
print(reversed_num)