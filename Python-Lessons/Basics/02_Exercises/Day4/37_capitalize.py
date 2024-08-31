# ---Capitalize first letter of each word without using .title()---

s = input("Enter the sentence: ")
word = ""
for i in s:
    if i == " ":
        print(word.capitalize(), end=" ")
        word = ""
    else:
        word += i
print(word.capitalize())