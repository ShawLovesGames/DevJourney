# ---Ask the user for their age, check if they are eligible to vote (≥18)---

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")