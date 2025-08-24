# ---Ask for age and nationality, only allow voting if age ≥ 18 and nationality is "Indian"---

age2 = int(input("Enter your age: "))
nat = input("Enter your nationality (first letter capital): ")
if age2 >= 18:
    if nat == "Indian":
        print("You are eligible to vote.")
    else:
        print("You are not a citizen of India and cannot vote.")
else:
    print("You are a minor and hence cannot vote.")