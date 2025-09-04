# ---Check if a string is a palindrome (case-insensitive)---

s = input("Enter the string: ")
lower = s.lower()
reverse = ""
for i in lower:
    reverse = i + reverse
if reverse == lower:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")