# ---WAP to replace all vowels with an asterisk in a string---

s = input("Enter a string: ")
newString = ""
for i in s:
    if i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U':
        newString += '*'
    else:
        newString += i
print(newString)