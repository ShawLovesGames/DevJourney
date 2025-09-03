# ---Count how many words start and end with the same letter---

s = input("Enter the string: ")
word = ""
count = 0
for i in s:
    if i != " ":
        word += i
    else:
        if word and word[0].lower() == word[-1].lower():
            count += 1
        word = ""
if word and word[0].lower() == word[-1].lower():
    count += 1
print(count)

# Just realised I can use just "word" for truthyness