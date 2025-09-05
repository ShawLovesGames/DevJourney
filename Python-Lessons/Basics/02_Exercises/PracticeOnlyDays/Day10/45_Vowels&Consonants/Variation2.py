# ---Count vowels and replace them with * in the output string---

s = input("Enter the string: ")
newString = ""
for i in s:
    if i.isalpha:
        if i in "aeiouAEIOU":
            newString += "*"
        else:
            newString += i
print(newString)