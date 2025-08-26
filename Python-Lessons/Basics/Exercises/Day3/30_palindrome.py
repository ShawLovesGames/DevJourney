n = int(input("Enter the number of palindromes: "))
count = 0
original_num = 1
reversed_num = 0
while count < n:
    temp = original_num
    reversed_num = 0
    while temp > 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp = temp // 10
    if reversed_num == original_num:
        print(reversed_num)
        count += 1
    original_num += 1