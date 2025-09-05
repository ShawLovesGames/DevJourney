# ---Reverse the order of characters inside every second word only---

s = input("Enter the string: ")
count = 0
word = ""
newString = ""
for i in s:
    if i.isalpha():
        word += i
    else:
        count += 1
        if count % 2 == 0:
            newString += word[::-1]
        else:
            newString += word
        word = ""
        newString += i
count += 1
if count % 2 == 0:
    newString += word[::-1]
else:
    newString += word
print(newString)