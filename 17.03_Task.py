# # Task 1. Write a  program three integer number by using input function

print("\nWrite a  program three integer number by using input function:-")

a = int(input("Enter First number:"))
b = int(input("Enter Second number:"))
c = int(input("Enter third number:"))

if a > b and a > c :
    print("First number is the greatest number!")
elif b > a and b > c:
    print("Second number is the greatest number!")
else:
    print("Third number is the greatest number!")


# Task 2. write a program to get a loan by using nested if.

print("\nWrite a program to get a loan by using nested if:-")

age = int(input("Enter your age :"))
salary = int(input("Enter your monthly salary:"))

if age >= 18:
    if salary >= 25000:
        print("Loan approved!")
    else:
        print("Loan Rejected: Salary is too low")
else:
    print("Age must be 18 or above")