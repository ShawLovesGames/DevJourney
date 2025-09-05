# ---Count vowels only in the first half of the string and count consonants in the entire string---

s = input("Enter the string: ")
vowel = 0
conso = 0
count = 0
halfString = int(len(s)/2)
for x in s:
    if x.isalpha():
        if x in "aeiouAEIOU":
            vowel += 1
    count += 1
    if count == halfString:
        break          
for i in s:
    if i.isalpha():
        if i not in "aeiouAEIOU":
            conso += 1
print(f"The number of vowels is: {vowel}")
print(f"The number of consonants is: {conso}")