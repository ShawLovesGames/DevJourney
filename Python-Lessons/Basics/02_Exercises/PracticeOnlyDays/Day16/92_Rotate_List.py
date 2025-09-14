# ---Write a program that rotates a list to the right by 2 positions---

lst = [1, 2, 3, 4, 5]
i = int(input("Enter the number of positions to rotate: "))

rotated = lst[-i:] + lst[:-i]
print(rotated)