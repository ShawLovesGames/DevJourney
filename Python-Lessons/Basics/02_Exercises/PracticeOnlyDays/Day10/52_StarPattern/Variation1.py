# ---Print pattern for n = 4---
# ****
# ***
# **
# *

n = int(input("Enter the number of rows: "))
for i in range(n, 0, -1):
    print('*'*i)