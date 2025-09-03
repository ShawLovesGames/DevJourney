# ---Remove all punctuation from a string---

s = input("Enter the string: ")
for i in s:
    if i in ",.?!:;'":
        continue
    else:
        print(i, end="")