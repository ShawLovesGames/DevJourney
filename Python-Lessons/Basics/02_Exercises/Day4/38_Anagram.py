# ---Check if two strings are anagrams of each other---

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
if len(s1) != len(s2):
    print("Not Anagrams.")
else:
    is_anagram = True
    for i in s1:
        if s1.count(i) != s2.count(i):
            is_anagram = False
            break
    if is_anagram:
        print("They are anagrams.")
    else:
        print("Not anagrams.")