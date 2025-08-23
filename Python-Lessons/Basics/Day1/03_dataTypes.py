# Learning Variables

# Variables are names of memory location used to store a value and access the value to perform various operations or tasks.
name = "Akshat Shaw" # Name variable containing String value
age = 20 # Age variable containing Int value
marks = 85.5 # Marks variable containing Float value
isAdult = True # isAdult variable containing boolean value
friends = None # Friends variable containing none type value

# Printing the variables
print(name)
print(age)
print(marks)
print(isAdult)
print(friends)

# Printing the types of the variables
print(type(name))
print(type(age))
print(type(marks))
print(type(isAdult))
print(type(friends))

# We can explicitly change the data type of a variable using type casting
age = str(age) # Changing age variable from int to string
print(age)
print(type(age))