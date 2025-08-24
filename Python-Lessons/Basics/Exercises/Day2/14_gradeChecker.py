# ---Grading System – Take marks and print the grade:--- 
# ---90–100: A+--- 
# ---80–89: A--- 
# ---70–79: B--- 
# ---60–69: C--- 
# ---<60: Fail--- 

marks = float(input("Enter your marks: ")) 
if marks > 100 or marks < 0: 
    print("Invalid marks!")
elif marks >= 90:
    print("Your grade is A+.")
elif marks >= 80 and marks <= 89:
    print("Your grade is A.")
elif marks >= 70 and marks <= 79:
    print("Your grade is B.")
elif marks >= 60 and marks <= 69:
    print("Your grade is C.")
else: print("You have failed your exam.")