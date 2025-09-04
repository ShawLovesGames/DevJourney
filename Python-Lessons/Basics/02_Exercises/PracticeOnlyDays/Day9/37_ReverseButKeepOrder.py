# ---Reverse each word but keep the word order in a string---

s = input("Enter a string: ")
word = ""
reverse = ""
for i in s:
    if i != " ":
        word += i
    else:
        for j in word[::-1]:
            reverse += j
            word = ""
        reverse += " "
for k in word[::-1]:
    reverse += k
print(reverse)