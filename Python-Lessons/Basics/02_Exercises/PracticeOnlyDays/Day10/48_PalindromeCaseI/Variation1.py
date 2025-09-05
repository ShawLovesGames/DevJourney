# ---Ignore spaces and punctuation while checking---

s = input("Enter the string: ")
newString = ""
for i in s:
    if i.isalpha():
        newString += i
if newString == newString[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")