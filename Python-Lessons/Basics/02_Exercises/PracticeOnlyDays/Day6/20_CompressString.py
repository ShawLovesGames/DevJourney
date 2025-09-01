# ---Compress a string by replacing repeated characters with the character followed by the count---

s = input("Enter the string: ")
repeated = ""
for i in s:
    if i not in repeated:
        if s.count(i) > 1:
            print(i, end="")
            print(s.count(i), end="")
            repeated += i
        else:
            print(i, end="")
            print(s.count(i), end="")