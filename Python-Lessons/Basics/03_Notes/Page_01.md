# **Notes #1**

---

### **Print statement**
- The print() function prints the specified message to the screen, or other standard output device
- Syntax example - print(20)

### **Comments**
- Comments are used to explain Python code and they make the code more readable
- Comments are either single line which are written using #, or
- Comments can also be multi line which are written enclosed in """

### **Modules**
- A module is a file containing a set of functions you want to include in your application
- More about modules later
- For example - I installed pyjokes and used it to print a random joke

### **Variables**
- Variables are containers for storing data values
- In python, we do not need to explicitly declare the data type before creating and initializing a variable
- They are created when we first assign a value to it, example :- x = 1 (now x is a variable of type int that contains the integer 1)
- **Casting** is used to either specify the type of variable, or to change the type of an existing variable, example :- x = str(1) (now x is a variable of type str that contains the string '1')
- We can use *type()* function to get the data type of a variable
- Both single qoutes and double qoutes can be used to declare strings. The better habit to have is to use single qoutes for characters and double qoutes for strings
- Variable are case sensitive. Therefore A = 1 and a = 1 are different variables
- ##### **Naming Rules**
    - A variable name must start with a letter or the underscore character
    - A variable name cannot start with a number
    - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    - A variable name cannot be any of the Python keywords
- ##### **Naming techniques**
    - *Camel Case* Each word, except the first, starts with a capital letter: myAge = 20
    - *Pascal Case* Each word starts with a capital letter: MyFullName = "Akshat Shaw"
    - *Snake Case* Each word is separated by an underscore character: my_full_name = "Akshat Shaw"
- ##### **Assigning Multiple Values**
    - We can assign values to multiple variables in one line. Example :- x, y, z = 1, 2, 3
    - We can also assign the same value to multiple variables in one line. Example :- x = y = z = 5
- ##### **Output Variables**
    - The print() function is commonly used to output variables. Example :- print(a)
    - We can separate multiple variables using comma to print multiple variables with one print statement. Example :- print(a, b)
    - We can use the + operator to combine two variables. For strings this is concatenation and for numbers this acts as the addition operator. Example :- print(a + b)
    - The comma adds a space between variable values. Example :- print(x, y) | Output :- 5 5
- ##### **Global variables**
    - We can define variables outside of a function (in the main code) and use them in the function
    - If we create a variables of the same name inside a function, the variable inside the funtion will be local and it can only be used inside the function
    - To create global variables inside function we can use the global keyword.
    - We can also use the global keyword inside a function to change the value of an existing global variable.

### **Data Types**
- Variables can store data of different types. Different types of data can do different things
- The data types built-in python are :- str, bool, int, float, complex, list, tuple, range, dict, set, frozenset, bytes, bytearray, memoryview, NoneType
- Python allows explicit type casting ; We can change the data types manually
- Unlike other programming languages we do not have to explicitly state the data type before creating a variable
- Python sets the data type by itself
- Other than built-in data types there are user defined data types or reference data types

### **Strings**
- Strings are collections of characters. They are surrounded by either single or double qoutes
- Like many popular programming languages strings are arrays of unicode characters but,
- Python does not have a character data type and a single character is a string of length of 1
- Strings are immutable and every function used to manipulate a string returns a new string and does not effect the existing string
- Strings are indexed and with indexes we can slice strings. The first character has index 0

### **Lists**
- Lists are used to store multiple items in a single variable. It is created using square brackets
- Lists are ordered, therefore they have a defined order and the order will not change
- List items are mutable. The items in the list can be changed, added or removed even after it has been created
- Lists can store multiple data types. A string, an integer, a boolean value or a decimal number can all be stored in one list
- Lists are indexed and the first item will have index 0

### **Tuples**
- Tuples are also used to store multiple items in a single variable. It is created using round brackets
- Tuples are immutable. The items in the tuple never change unless we use the list() constructor trick
- They are indexed like lists and the first item will have index 0
- They are ordered like lists and the defined order cannot change
- Tuples can also store items of different data types

### **Sets**
- Sets are also used to store multiple items in a single variable. It is created using curly brackets
- Set items are unordered, they do not have a defined order. We cannot refer to set items using their index
- Set items are unchangeable, we cannot change the items but we can remove existing items or add new items
- Sets do not allow duplicates
- Sets can also store items of different data types

### **Dictionaries**
- Dictionaries are used to store data values in key:value pairs, they are created using curly brackets
- Dictionaries are ordered since python version 3.7. Earlier they were undeordered
- Dictionaries are changeable
- Dictionaries do not allow duplicates

### **Functions**
- Functions are blocks of code that run when they are called
- We can pass data, knows as parameters, into a function
- Functions can return data as a result
- Functions are created using the def keyword
- ##### **Parameters**
    - A parameter is the variable listed inside the parentheses in the function definition
- ##### **Arguments**
    - An argument is the value that is sent to the function when it is called