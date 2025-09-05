# ---Reverse only words that contain digits---

s = input("Enter the string: ")
word = ""
newString = ""
for i in s:
    if i != " ":
        word += i
    else:
        has_digit = False
        for j in word:
            if j.isdigit():
                has_digit = True
                break
        if has_digit:
            newString += word[::-1]
        else:
            newString += word
        newString += i
        word = ""
has_digit = False
for j in word:
    if j.isdigit():
        has_digit = True
        break
if has_digit:
    newString += word[::-1]
else:
    newString += word
print(newString)