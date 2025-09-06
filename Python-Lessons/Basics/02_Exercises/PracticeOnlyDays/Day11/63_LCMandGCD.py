# --LCM and GCD - Find both for two numbers---

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
limit = 0
GCDis = 0
if n1 == 0 and n2 == 0:
    print("Invalid!")
if n1 > n2:
    limit = n2
else:
    limit = n1
for i in range(1, limit):
    if n1 % i == 0 and n2 % i == 0:
        GCDis = i
LCMis = (n1*n2) // GCDis
print("The GCD of the two numbers is: ", GCDis)
print("The LCM of the two numbers is: ", LCMis)