# ---While Loop---

# The while loop is used to execute a set of statements as long as a condition is true.

num = 1
while num <= 10: # This statement means while num is lesser than or equal of 10, the following suite should be executed.
    print("Hello!") # This print statement will be executed multiple times until num is greater than 10.
    num += 1 # Without incrementing the loop will become infinite as num will always stay at 1 and the condition will always be true.
# Output will be "Hello!" 10 times.

# ---Break Statement---

num1 = 1
while num1 <= 10:
    print(num1)
    if num1 == 5: # if statement to check if the value of num1 is 5.
        break # Exiting the loop with the break statement.
    num1 += 1
# Output will be 1 2 3 4 5. Because the loop will be stopped by the break statement when the value of num1 is 5.

# ---Continue Statement---

num2 = 1
while num2 <= 10:
    num2 += 1
    if num2 == 5: # if statement to check if the value of num2 is 5.
        continue # Continue statement is used to skip the current iteration.
    print(num2)
# Output will be 1 2 3 4 6 7 8 9 10. Because when num2's value reaches 5 we skip the iteration.

# ---Else statement usage with While---

num3 = 5
while num3 <= 50:
    print(num3)
    num3 += 5
else: # We can use the else statement to run a suite after the loop is over.
    print("Table of 5!")