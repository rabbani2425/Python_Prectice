'''Assignment on if and else '''

'''1. Big or Small number ''' 
# Take an integer input from the user.if it is greter than 100. print "Big Number",else prine "Small number "

num = int(input("Enter a nummber:"))
if num > 100:
    print("Big Number")
else:
    print("Small Number")
# --------------------------------------------

'''2.Senior Citizen or Adult'''
# ask the user for their name and age. if age is 60 or more, print "Senior Citizen",otherwise print"Adult"

name = input("Enter your name:")
age = int(input("Enter your age:"))
if age >=60:
    print("Senior Citizen")
else:
    print("Adult")

# --------------------------------------------

'''3. Find Large of two number '''
# Ask for two numbers and print the larger one using if-else

num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))
if num1 > num2:
    print("Large number is:",num1)
else:
    print("Large number is:",num2)

# --------------------------------------------

'''4. Password Checker '''
# ask for a password. if the entered password is "gulam@2425", print"Login Seccessfull",else print "Access Denied"

password = input("Enter your password:")
if password == "gulam@2425":
    print("Login Seccessfull")
else:
    print("Access ")