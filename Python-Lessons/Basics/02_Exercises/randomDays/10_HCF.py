# ---HCF (Highest Common Factor) of two numbers without using any built-in functions---

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
x = False
i = 0
hcf = 0
if n1 > n2:
    i = n1 - 1
else:
    i = n2 - 1
while x == False:
    for j in range(i, 1, -1):
        if n1 % j == 0 and n2 % j == 0:
            hcf = j
            x = True
            break
print(hcf)