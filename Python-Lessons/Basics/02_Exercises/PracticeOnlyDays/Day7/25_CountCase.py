# ---WAP to count uppercase and lowercase letters separately---

s = input("Enter the string: ")
upper = 0
lower = 0
for i in s:
    if i.isalpha():
        if i.isupper():
            upper += 1
        else:
            lower += 1
    else:
        continue
print(f"Upper case letters : {upper} || Lower case letters : {lower}")