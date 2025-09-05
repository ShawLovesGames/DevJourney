# ---Find the longest word in a sentence (no .split())---

s = input("Enter the string: ")
max_word = ""
current_word = ""
for i in s:
    if i.isalpha():
        current_word += i
    else:
        if len(max_word) < len(current_word):
            max_word = current_word
        current_word = ""
if len(max_word) < len(current_word):
    max_word = current_word
print(max_word)