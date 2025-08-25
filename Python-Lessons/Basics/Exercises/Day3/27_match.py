# ---Use match to take a day number (1–7) and print the name of the day---

day = int(input("Enter the number of day (1-7): "))
match day:
    case 1:
        print("Monday!")
    case 2:
        print("Tuesday!")
    case 3:
        print("Wednesday!")
    case 4:
        print("Thursday!")
    case 5:
        print("Friday!")
    case 6:
        print("Saturday!")
    case 7:
        print("Sunday!")