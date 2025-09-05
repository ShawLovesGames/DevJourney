# ---Check rotation ignoring case and punctuation---

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
lowerS1 = s1.lower()
lowerS2 = s2.lower()
cleanedS1 = ""
cleanedS2 = ""
for i in lowerS1:
    if i.isalpha():
        cleanedS1 += i
for j in lowerS2:
    if j.isalpha():
        cleanedS2 += j
if len(cleanedS1) != len(cleanedS2):
    print("They are not a rotation.")
elif cleanedS2 in cleanedS1 + cleanedS1:
    print("They are a rotation.")
else:
    print("They are not a rotation.")