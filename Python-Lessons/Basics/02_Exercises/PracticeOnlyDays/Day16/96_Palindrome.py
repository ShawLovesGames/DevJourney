# ---Write a program to check if a tuple is a palindrome---

tup = (1, 2, 3, 2, 1)

if tup == tup[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")