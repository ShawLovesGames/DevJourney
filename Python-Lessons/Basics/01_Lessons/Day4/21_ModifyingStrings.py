# ---Modifying Strings using methods---

# We can use built in methods to modify strings.
# Note :- As strings are immutable, the original string is not changed by the methods. What happens is that a new object is created which is the modified version of the strings.

s = " Hello, World! "

#1 Upper case.
print(s.upper()) # The upper method returns the string in upper case.

#2 Lower case.
print(s.lower()) # The lower method returns the string in lower case.

#3 Remove whitespace.
print(s.strip()) # The strip method removes all whitespace from beginning or the end and returns the string.

#4 Replace string.
print(s.replace('H', 'J')) # The replace method replaces a string with another string. s.replace("String to be replaced", "New string to be added").

#5 Split string.
print(s.split(',')) # The split method returns a list that contains substrings which are splitted from the string at the instance of the separator (in this case - ',').