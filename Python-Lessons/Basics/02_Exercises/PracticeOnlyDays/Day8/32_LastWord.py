# ---Find the last word in a sentence without .split()---

s = input("Enter the string: ")
word = ""
for i in s:
    if i == " ":
        word = ""
    else:
        word += i
print(word)