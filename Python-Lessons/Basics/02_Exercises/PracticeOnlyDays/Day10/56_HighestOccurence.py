# ---Find the most frequent character (ignore case and spaces)---

s = input("Enter the string: ")
text = s.lower().replace(" ", "")
highest = text[0]
for i in text:
    if text.count(i) > text.count(highest):
        highest = i
print(highest)