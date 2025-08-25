# ---Print a triangle pattern using nested loops:---
# ---*---
# ---**---
# ---***---
# ---****---
# ---*****---

rows = int(input("Enter the number of rows: "))
for x in range(1, rows+1):
    print("*" * x)