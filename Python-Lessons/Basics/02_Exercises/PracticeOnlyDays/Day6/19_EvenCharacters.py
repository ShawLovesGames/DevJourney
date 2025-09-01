# ---Count words with even length in a given string---

s = input("Enter the sentence: ")
word = ""
even = 0
for i in s:
    if i != " ":
        word += i
    else:
        if len(word) % 2 == 0:
            even += 1
        word = ""
if len(word) % 2 == 0:
    even += 1
print(f"Number of words with even length: {even}")