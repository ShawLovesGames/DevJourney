# ---Count words with even length but replace them with * in the output---

s = input("Enter the string: ")
word = ""
newString = ""
count = 0
for i in s:
    if i.isalpha():
        word += i
    else:
        if word and len(word) % 2 == 0:
            newString += '*'
            count += 1
        else:
            newString += word
        newString += i
        word = ""
if word and len(word) % 2 == 0:
    newString += '*'
    count += 1
else:
    newString += word
print(count)
print(newString)