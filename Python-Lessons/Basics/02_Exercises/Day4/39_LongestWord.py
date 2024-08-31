# ---Find the longest word in a sentence---

s = input("Enter the sentence: ")
current = ""
longest = ""
for i in s:
    if i != " ":
        current += i
    else:
        if len(current) > len(longest):
            longest = current
            current = ""
        else:
            current = ""
if len(current) > len(longest):
            longest = current
print(longest)