# ---String formatting---

# F-strings was introduced in python 3.6.
# We can put a f in front of the string literal and use curly brackets {} with variables and other operations inside.
name = "Akshat Shaw"
age = 20
n = 7
intro = f"My name is {name} and I am {age} years old." # {} are placeholders.
print(intro)

# ---Placeholders and Modifiers---

# Placeholders are like holes than python can fill. They can contain variables, operations, functions, and modifiers to format the value.
pi = 3.14159265
print(f"The value of pi is {pi}")

# Modifiers control how the value looks. They are included by adding a colon : followed by a legal formatting type.
print(f"The value of pi till two numbers after decimal is {pi:.2f}") # Numbers formatting.
print(f"The value of pi is {pi:5}") # Padding (width).
print(f"My code name is {n:03}") # Padding with zeros.
print(f"{name:^10}") # Align text.
 
# A placeholder can contain python code, like math operations.
price = f"The price is ${12 * 5}"
print(price)