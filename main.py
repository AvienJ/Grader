# NAME: Grader
# FILE: main.py(DIR: .\)

# DESCRIPTION: "The main file of Grader"
# CREDITS: Avien Jones(GITHUB: AvienJ)
# MISC\NOTES: 
# ____________________
import clear
import sys

def grade():
    ui_total = input("Enter amount of points total: ")
    clear.clear()
    ui_points = input("Enter amount of points earned: ")
    clear.clear()
    ui_extra = input("Extra points?: ")
    clear.clear()
    percentage = (float(ui_points) + float(ui_extra)) / float(ui_total) * 100
    grade = ""
    
    if 90 <= percentage >= 100:
        grade = "A"
    elif 70 <= percentage <= 89:
        grade = "B"
    elif 60 <= percentage <= 79:
        grade = "C"
    elif 50 <= percentage <= 69:
        grade = "D"
    elif percentage <= 59:
        grade = "F"

    if percentage == int(percentage):
        print (str(int(percentage)) + "%| " + grade)
        ui_end = input('Press "Enter" to continue...')
    else:
        print (str(percentage) + "% | " + grade)
        ui_end = input('Press "Enter" to continue...')

while True:
    clear.clear()
    grade()
