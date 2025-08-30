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