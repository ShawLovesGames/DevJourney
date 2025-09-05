# ---Count only words with even length and starting with consonant---

s = input("Enter the string: ")
word = ""
count = 0
for i in s:
    if i.isalpha():
        word += i
    else:
        if word and word[0] not in "aeiouAEIOU":
            if len(word) % 2 == 0:
                count += 1
        word = ""
if word and word[0] not in "aeiouAEIOU":
    if len(word) % 2 == 0:
        count += 1
print(count)