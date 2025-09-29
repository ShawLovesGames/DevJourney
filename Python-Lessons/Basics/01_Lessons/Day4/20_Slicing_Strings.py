#** ---String Slicing--- 

# We can slice strings to print a range of characters from the string.
s = "Hello World!"
print(s[1:5]) # Output :- ello
# Note :- First character has index 0.
# Note :- The last index (in this case - 5) is excluded.

# Slicing from the start.
print(s[:5]) # Output :- Hello
# We can leave out the first index in order to slice from the start.

# Slicing to the end.
print(s[6:]) # Output :- World!
# We can leave out the last index in order to slice from the given index to the end of the string. Very useful imo.

# ---Negative Indexing---

# Python allows negative indexing.
print(s[-12:-7])
# Note :- The last character of a string has index -1.
# Note :- The last index (in this case :- -7) is excluded.