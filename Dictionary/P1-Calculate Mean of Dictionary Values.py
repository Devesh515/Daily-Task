# 1. Write a Python program and calculate the mean of the below dictionary. Accept student anme as key and in value accept marks

# Create an empty dictionary to store student names and marks
student_marks = {}

# Ask the user for the number of students
num_students = int(input("Enter the number of students: "))

# Accept student names and marks from the user
for _ in range(num_students):
    name = input("Enter student's name: ")
    marks = float(input(f"Enter {name}'s marks: "))
    student_marks[name] = marks

# Calculate the total marks
total_marks = 0
for marks in student_marks.values():
    total_marks += marks

# Calculate the number of students
num_students = len(student_marks)

# Calculate the mean (average) marks
mean_marks = total_marks / num_students

# Print the mean marks
print("The mean marks of the students is:", mean_marks)

