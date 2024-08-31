# ---Reverse each word in a sentence without changing word order---

s = input("Enter a sentence: ")
word = ""
reversed_word = ""
for i in s:
    if i != " ":
        word += i
    else:
        reversed_word = ""
        for i in word:
            reversed_word = i + reversed_word
        print(reversed_word, end=" ")
        word = ""
reversed_word = ""
for i in word:
    reversed_word = i + reversed_word 
print(reversed_word)