# ---Print all even numbers between 1 and 50 using a for loop with range()---

# Method 1
for x in range(1, 51):
    if x % 2 == 0:
        print(x)
    else:
        continue

# Method 2
for x in range(2, 51, 2):
    print(x)