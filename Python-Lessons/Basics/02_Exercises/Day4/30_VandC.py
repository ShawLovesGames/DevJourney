# ---Count vowels and consonants in a given string---

s = input("Enter a string in all small letters: ")
vowels = 0
cons = 0
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowels += 1
    else:
        cons += 1
print(f"The number of vowels in the string: {vowels}")
print(f"The number of consonants in the string: {cons}")