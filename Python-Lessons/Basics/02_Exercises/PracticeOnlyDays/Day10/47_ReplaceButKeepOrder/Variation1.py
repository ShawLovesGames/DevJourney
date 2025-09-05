# ---Reverse only words that start with a vowel---

s = input("Enter the string: ")
word = ""
newString = ""
for i in s:
    if i.isalpha():
        word += i
    else:
        if word[0] in "aeiouAEIOU":
            newString += word[::-1]
        else:
            newString += word
        newString += i
        word = ""
if word[0] in "aeiouAEIOU":
    newString += word[::-1]
else:
    newString += word
print(newString)