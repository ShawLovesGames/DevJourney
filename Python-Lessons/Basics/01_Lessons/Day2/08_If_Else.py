# ---Conditional Statements---

# Condtional statements lets my code make decisions based on whether something is true or false.
# In python, indentation is used to define the scope of a keyword like if. Unlike C that uses curly brackets {}.

# ---If-else statements---
num1 = 1 # Initializing two variables with values.
num2 = 2
if num1 > num2: # Using if keyword to check if a given condition is true.
    print(str(num1) + " is greater.") # If the statement is true the suite (block of code) under the if statement is run. 
else: # Using else keyword to run another suite in case the given condition is false.
    print(str(num2) + " is greater.")

# Pass statement can be used if we want an if statement which does not have a suite. Without the pass statement we would have an error.
if num1 <= num2:
    pass

# ---Chained comparisons---
if 0 < num1 < 3: # Chained comparison in one given statement. Valid.
    print("Num1 is greater than 0 but lesser than 3")
else:
    print("Num1 is either lesser than 0 or greater than 3")