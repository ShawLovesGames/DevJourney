# ---Count vowels & consonants separately in a string---

s = input("Enter the string: ")
vowel = conso = 0
for i in s:
    if i.isalpha():
        if i in "aeiouAEIOU":
            vowel += 1
        else:
            conso += 1
print(f"The number of vowels: {vowel}")
print(f"The number of consonants: {conso}")