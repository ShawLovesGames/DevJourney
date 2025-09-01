# ---Check if one string is a rotation of another string---

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
if len(s1) != len(s2):
    print("Not a rotation.")
elif s2 in s1 + s1:
    print("It is a rotation.")
else:
    print("Not a rotation.")