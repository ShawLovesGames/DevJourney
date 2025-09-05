# ---Convert even-indexed letters to uppercase, odd to lowercase (ignore spaces for counting)---

s = input("Enter the string: ")
newString = ""
count = 0
for i in s:
    if i.isalpha():
        if count % 2 == 0:
            newString += i.upper()
        else:
            newString += i.lower()
        count += 1
    else:
        newString += i
print(newString)