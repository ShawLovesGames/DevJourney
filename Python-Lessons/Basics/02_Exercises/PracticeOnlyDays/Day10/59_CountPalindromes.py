# ---Count words that are palindromes in a string---

s = input("Enter the string: ")
word = ""
count = 0
for i in s:
    if i.isalpha():
        word += i
    else:
        if word.lower() == word.lower()[::-1]:
            count += 1
        word = ""
if word.lower() == word.lower()[::-1]:
    count += 1
print(count)