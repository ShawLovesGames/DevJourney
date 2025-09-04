# ---Count words with even length, ignoring punctuation in a string---

s = input("Enter a string: ")
count = 0
word = ""
for i in s:
    if i.isalpha():
        word += i
    else:
        if word:
            if len(word) % 2 == 0:
                count += 1
            word = ""
if len(word) % 2 == 0:
    count += 1
print(f"The number of words with even length are: {count}")