import sys
import os

GPA = 0
allCredits = 0
allGradePoints = 0
grade = ""
print("Welcome to term GPA calculator!")
userinput = input("Write start or exit: ")

while True:
    GPA = 0
    allCredits = 0
    allGradePoints = 0
    grade = ""

    while userinput.lower() != "exit":
        grade = input("Please enter your grade: ")
        if grade == "end":
            break
        
        gradeNumber = 0
        gradePoint = 0
        credit = 0

        if grade.lower() == "a":
            gradeNumber = 4.0
        elif grade.lower() == "a-":
            gradeNumber = 3.7
        elif grade.lower() == "b+":
            gradeNumber = 3.3
        elif grade.lower() == "b":
            gradeNumber = 3.0
        elif grade.lower() == "b-":
            gradeNumber = 2.7
        elif grade.lower() == "c+":
            gradeNumber = 2.3
        elif grade.lower() == "c":
            gradeNumber = 2.0  
        elif grade.lower() == "c-":
            gradeNumber = 1.7 
        elif grade.lower() == "d+":
            gradeNumber = 1.3
        elif grade.lower() == "d":
            gradeNumber = 1.0
        elif grade.lower() == "d-":
            gradeNumber = 0.7
        elif grade.lower() == "f":
            gradeNumber = 0.0

        credit = int(input("Please enter the credit of the class: "))
        gradePoint = credit * gradeNumber

        allCredits += credit
        allGradePoints += gradePoint

    if userinput.lower() == "exit":
        print("Quitting...")
    else:    
        if allCredits == 0: # solution to zero division error
            print("An error occurred. Possibly caused by the lack of credit input.")
        else:
            GPA = allGradePoints / allCredits
            print("Your term GPA is", format(GPA,".2f"))

        question = input("Would you like to start over? ")

        if question == "yes":
            print("Restarting the calculator...")
        elif question == "no":
            print("Alright, thank you for using the calculator!")
            sys.exit()


    





