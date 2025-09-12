# ---Create a tuple with duplicate values. Print how many times a given element appears (without using .count())---

my_tuple = (1, 2, 3, 2, 1, 3, 4, 4, 5, 1)
print(my_tuple)

target = int(input("Enter the target element from the tuple: "))

count = 0

for i in my_tuple:
    if i == target:
        count += 1

print(f"{target} occurred {count} times.")