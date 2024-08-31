# ---Remove duplicates from a string while keeping order---

s = input("Enter the string: ")
temp = ""
for i in s:
    if i not in temp:
        print(i, end="")
        temp += i