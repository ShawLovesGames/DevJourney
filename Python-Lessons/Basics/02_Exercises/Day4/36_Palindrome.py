# ---Check palindrome---

s = input("Enter a string: ")
reversed_string = ""
for i in s:
    char = i
    reversed_string = char + reversed_string
if reversed_string == s:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")