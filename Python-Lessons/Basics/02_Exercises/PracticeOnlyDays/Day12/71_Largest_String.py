# ---Given a list of strings, print the string with the maximum length---

lst = ["AAA", "BBBB", "CCCC", "DDDDD"]
largest = ""
for i in lst:
    if len(i) > len(largest):
        largest = i
print(largest)