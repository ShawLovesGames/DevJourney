# ---Convert uppercase letters to lowercase and lowercase to uppercase without using the built-in swapcase function---

s = input("Enter a string: ")
for i in s:
    if i.isupper():
        print(i.lower(), end="")
    else:
        print(i.upper(), end="")    