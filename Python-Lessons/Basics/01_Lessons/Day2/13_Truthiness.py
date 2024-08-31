#* ---TRUTHINESS---

surname = ""
if surname: # Empty strings, Zero and None are falsey.
    print("Truthy")
else:
    print("Falsey")

if not surname:  # Checks if surname is falsy.
    print("Surname not provided.")