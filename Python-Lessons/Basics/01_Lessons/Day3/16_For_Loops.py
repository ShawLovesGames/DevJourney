# ---For loop---

for x in "Akshat": # A for statement is used to iterate over a sequence (It is different from the for loop in other programming languages).
    print (x) # Prints every letter from the string "Akshat"

#1 Note:- For statement has many uses with lists, tuples, dictionaries, sets and strings which I will learn in the near future.
#2 Note:- For statement does not require an indexing variable to set beforehand.

# ---Break statement---

for x in "Akshat":
    print(x)
    if x == 'h':
        break # The break statement can be used to end the for loop prematurely as per our needs.
# Prints the letters 'A' 'k' 's' 'h'.

# ---Continue statement---

for x in "Akshat":
    if x == 'h':
        continue # The continue statement can be used to skip the current iteration as per our needs.
    print(x)
# Prints the letters 'A' 'k' 's' 'a' 't'.

# ---Range Statement---

for x in range(6): # To loop through a set of code, a specific number of times. We use the range() function.
    print(x)
# Prints 0 1 2 3 4 5. Note:- Range(6) is not values 0-6 but 0-5.

for x in range(2, 6): # Using start parametre.
    print(x)
# Print 2 3 4 5. Note:-  Values 2-6 but not including 6.

for x in range(5, 51, 5): # Using third parametre to increment by 5. Note:- Default is 1.
    print(x)
# Prints 5 10 15 20 25 30 35 40 45 50. Always increments by 5.

# ---Else statement usage in for loop---

for x in range(2, 21, 2):
    print(x)
else: # Else statement with a for loop is used to run a suite after the loop is finished.
    print("The table of 2.") 
# Note:- The else statement will not run if the loop was ended by a break statement.

# ---Nested loops---

for x in range(1, 4): # Outer loop.
    for y in range(1, 4): # Inner loop. Executed one time for each iteration of the outer loop.
        print(x + " " + y)

# ---Pass Statement---

for x in "Pass":
    pass # Pass statement is used when we need to have an empty for loop.