# Expression execution
n, txt = 2, "Hello " # String and numeric values can operate together with * and + (Adding strings is called concatenation).
print(txt * n)

n1, n2 = 2, 2.5 # Arithmetic operations with integers and floats results in float
print(str(n1 + n2) + "  " + str(n1 * n2) + "  " + str(n1 / n2) + "  " + str(n1 - n2) + "  " + str(n1 % n2))
# To concatenate int data type to strings we must convert them explicitly to strings using str().

print(n1//n2) # Integer division, result is an integer but displays as float
# Integer division is basically floor division from mathematics, it return the largest integer less than or equal to the reult.
# For example 5//2 = 2.0. Even a number like 4.99 will be rounded down to 4.0 while being closest to 5.