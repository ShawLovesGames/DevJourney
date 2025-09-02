# ---WAP to find the first non-repeating character in a string---

s = input("Enter a string: ")
for i in s:
    if s.count(i) == 1:
        print(i)
        break