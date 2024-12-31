NAME:Suhis Ragavan.M
COMPANY:CODTECH IT SOLUTION
ID:CT0806AU
DOMAIN:Python Programming
DURATION:dec 12 2024 to jan 12 2025
MENTOR:Sravani

OVER VIEW OF THIS PROJECT

Project:Develop a Python program to track and manage student grades.

Key Features
Dynamic Grade Tracking:
Tracks multiple subjects and grades.
Calculates subject-wise and overall averages.
Error Handling:
Prevents invalid grades and inputs.
Grade Evaluation:
Calculates overall GPA and converts grades to a letter scale.
User-Friendly Interface:
Menu-driven design for ease of use.
This program effectively demonstrates object-oriented programming principles, input validation, and user interaction in Python.

Class: GradeTracker
Attributes:

self.grades: A dictionary where keys are subjects (strings) and values are lists of grades (floats) for those subjects.
Methods:

add_grade(subject, grade):

Adds a grade for a specified subject.
If the subject is not in the dictionary, it initializes a new entry with an empty list.
Prints a confirmation message.
calculate_average():

Calculates the overall average grade across all subjects.
Returns 0 if no grades have been added.
calculate_gpa():

Converts the overall average grade into a GPA based on a standard 4.0 scale:
90+ → 4.0
80–89 → 3.0
70–79 → 2.0
60–69 → 1.0
Below 60 → 0.0
letter_grade():

Converts the overall average grade into a letter grade:
90+ → A
80–89 → B
70–79 → C
60–69 → D
Below 60 → F
display_summary():

Displays a summary of all grades by subject, including:
Grades for each subject.
The average grade for each subject.
Overall average grade, letter grade, and GPA.
Main Program
The main() function is the user interface for interacting with the GradeTracker. It provides a menu-driven system for user interaction.

Options Menu:

1. Add Grade:

Prompts the user to enter a subject and grade.
Ensures the grade is a valid numeric value between 0 and 100.
Calls the add_grade method.
2. Display Summary:

Calls the display_summary method to display:
Grades for each subject.
Subject-wise averages.
Overall average, letter grade, and GPA.
3. Exit:

Exits the program with a farewell message.
Input Validation:

Handles invalid numeric inputs for grades using a try-except block.
Ensures the entered grade is between 0 and 100.
Provides feedback for invalid menu choices.
