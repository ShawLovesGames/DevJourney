# ---The match statement selects one of many code blocks to be executed---

month = int(input("Enter the month number (1-12): "))
day = int(input("Enter the number of day of the week (1 to 7): "))
match day: # The match expression is evaluated once.
    case 1: # The value of the expression is compared with the values of each case. || In this case the comparison is - 'day == 1'
        print("Monday!") # If there is a match, the suite is executed.
    case 2: # Value is compared to 2.
        print("Tuesday!") # Will be executed if day == 2 is True
    case 3: # Value is compared to 3.
        print("Wednesday!")
    case 4: # Value is compared to 4.
        print("Thursday!")
    case 5: # Value is compared to 5.
        print("Friday!")
    case 6: # Value is compared to 6.
        print("Saturday!")
    case 7: # Value is compared to 7.
        print("Sunday!")
    case _: # _ case acts as the default case and will always match and hence is used when all other cases do not match (last).
        print("Not a valid day number:")

# '|' Character is used as an operator to combine values.
match day:
    case 1 | 2 | 3 | 4 | 5: # Same as - if day == 1 or day == 2 or day == 3 or day == 4 or day == 5: 
        print("Today is a weekday!")
    case 6 | 7:
        print("Today is a weekend!") # If the user gave 6 or 7 as input, "Today is a weekend!" will be printed.
    case _:
        print("Invalid!")

# ---if statements in the case evaluation are used as an extra condition-check---
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 1: # Using an if statement || Both the case check and if statement checks must be true for the following suite to be executed.
        print("A weekday in January.")
    case 1 | 2 | 3 | 4 | 5 if month == 2:
        print("A weekday in February.")
    case 1 | 2 | 3 | 4 | 5 if month == 3:
        print("A weekday in March.")
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April.")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May.")
    case 1 | 2 | 3 | 4 | 5 if month == 6:
        print("A weekday in June.") # If the day input is anywhere from 1-5 and the month input is 6 "A weekday in June." will be printed.
    case 1 | 2 | 3 | 4 | 5 if month == 7:
        print("A weekday in July.")
    case 1 | 2 | 3 | 4 | 5 if month == 8:
        print("A weekday in August.")
    case 1 | 2 | 3 | 4 | 5 if month == 9:
        print("A weekday in September.")
    case 1 | 2 | 3 | 4 | 5 if month == 10:
        print("A weekday in October.")
    case 1 | 2 | 3 | 4 | 5 if month == 11:
        print("A weekday in November.")
    case 1 | 2 | 3 | 4 | 5 if month == 12:
        print("A weekday in December.")