# ---WAP to count how many words start with a vowel---

s = input("Enter the sentence: ")
word = ""
count = 0
for i in s:
    if i != " ":
        word += i
    else:
        for j in word:
            if j == 'a' or j == 'A' or j == 'e' or j == 'E' or j == 'i' or j == 'I' or j == 'o' or j == 'O' or j == 'u' or j == 'U':
                count += 1
                word = ""
                break
            else:
                word = ""
                break
if j == 'a' or j == 'A' or j == 'e' or j == 'E' or j == 'i' or j == 'I' or j == 'o' or j == 'O' or j == 'u' or j == 'U':
    count += 1
print(count)