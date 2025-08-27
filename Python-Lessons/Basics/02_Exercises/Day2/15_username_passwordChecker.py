# ---Ask for a username and password, check if they match predefined ones---

username1 = "ShawShawShaw"
password1 = "IAintThatDumb"
username2 = input("Enter the username: ")
password2 = input("Enter the password: ")
if username2 == username1 and password2 == password1:
    print("Correct username and password! All of my bank accounts are now yours!")
else:
    print("Invalid username or password! All your bank accounts are now mine!")