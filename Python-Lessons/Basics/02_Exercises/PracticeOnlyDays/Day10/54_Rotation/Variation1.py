# ---Check if one string is a rotation OR a reverse of another---

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
if len(s1) != len(s2):
    print("The strings are neither a rotation nor a reverse.")
else:
    if s2 in s1 + s2  or s1 == s2[::-1]:
        print("The strings are either a rotation or a reverse.")
    else:
        print("The strings are neither a rotation nor a reverse.")