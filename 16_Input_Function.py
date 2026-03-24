'''Input Function in Python:-'''
# Input function is used to take input from the user in Python. It takes input as a string and returns it.

# Example:-
name = input("Enter your name: ") 
print("Hello, " + name + "!")

# # Example 2:-
age = input("Enter your age: ")
print("You are " + age + " years old.")
# ----------------------------------------------------------------------

# Input Function  - Add 2 numbers :-
# A simple program that takes two numbers as input from the user and prints their sum.
# prompting the user for the first number and second number 

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Since input() returns a string, we need to convert it to an integer 

num1 = int(num1)
num2 = int(num2)
# Calculating the sum  and display the result
sum = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum)

# ----------------------------------------------------------------------------

# Multiple Input form user & Handing different data types

# input form user to add two number and print result

x = input("Enter first number: ")
y = input("Enter second number: ")

# Casting input numbers to int to perform sum

# print("The sum of", x, "and", x, "is:", int(x) + int(x))

                #   or

print(f"The sum of {x} and {y} is: {int(x) + int(y)}")