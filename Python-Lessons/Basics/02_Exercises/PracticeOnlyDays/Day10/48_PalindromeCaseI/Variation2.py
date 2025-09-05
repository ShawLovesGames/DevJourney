# ---Check if the first and last words are palindromes---

s = input("Enter the string: ")
lower = s.lower()
first = ""
last = ""
for i in lower:
    if i.isalpha():
        first += i
    else:
        break
for j in lower[::-1]:
    if j.isalpha():
        last += j
    else:
        break
last = last[::-1]
if first == first[::-1] and last == last[::-1]:
    print("Both first and last words are palindromes.")
else:
    print("Both words are not palindromes.")