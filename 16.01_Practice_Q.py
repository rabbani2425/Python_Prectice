'''Write a program to input student name and marks in 3 subjects. Print name and percentage in output.'''

# Prompting the user for their name and 3 subjects marks 

name = input("Enter student name: ")
hindi_marks =input("Enter marks in Hindi: ")
english_marks = input("Enter marks in English: ")
math_marks = input("Enter marks in Math: ")

#  Calculating percentenge for 3 subjects
percentage = ((int (hindi_marks) + int(english_marks) + int(math_marks)) / 300) * 100

# Printing the final results
# print(f"Student Name: {name}")
# print(f"Percentage: {percentage:.2f}%")

                #   or
print(f"{name}, have {percentage}%. Well done & keep working hard!!")
