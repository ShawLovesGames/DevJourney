# ---Given a list of words, print only the words that have more than 4 letters---

lst = ["apple", "dog", "banana", "hi", "sun"]

for i in lst:
    if len(i) > 4:
        print(i, end=" ")