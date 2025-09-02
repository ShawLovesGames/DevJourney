# ---WAP to reverse the order of words (without using lists)---

s = input("Enter the sentence: ")
reverse = ""
word = ""
for i in s:
    if i != " ":
        word += i
    else:
        reverse = word + " " + reverse
        word = ""
reverse = word + " " + reverse
print(reverse.strip())