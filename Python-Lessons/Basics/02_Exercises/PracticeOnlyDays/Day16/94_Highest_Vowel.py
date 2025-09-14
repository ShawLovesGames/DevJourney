# ---Take a string input and print the word with the maximum number of vowels---

s = input("Enter the string: ")

words = s.split()
max_vowels = 0
vowel_word = ""

for word in words:
    count = 0
    for i in word:
        if i.lower() in "aeiou":
            count += 1
    if count > max_vowels:
        max_vowels = count
        vowel_word = word

print("Word with maximum vowels:", vowel_word)