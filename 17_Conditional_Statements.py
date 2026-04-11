# Conditional stmt => it is used to make decision in your code. 

# if 
# if - else 
# if- elif


Marks = int(input("enter your marks: "))

if Marks > 70 :
                    print("first Division")

if Marks > 60 and Marks < 70 :
                    print("Second Division")


'''example'''

age = int(input("Enter your age: "))
if age > 18 :
    print("You are eligible to vote.")


# if - else 
# => In if and else statement there are two conditions only

a = int(input("Enter your age: "))
if a > 18 :
    print("You are eligible to vote.")
else :
    print("You are not eligible to vote.")


# but

# if - elif - else

# => In if - elif - else statement there are three or more than two conditions.

a = int(input("Enter your number:"))
b = int(input("Enter your second number:"))

if a > b :
    print("a is greater than b")
elif a < b :
    print("b is greater than a")

else :
    print("a and b are equal")


a = int(input("Enter your marks: "))

if(a >= 90):
    print("Grade A+")
elif(80 <= a < 90):
    print("Grade A")
elif(70 <= a < 80):
    print("Grade B+")
elif(60 <= a < 70):
    print("Grade B")
else:
    print("Grade F")



'''Nested if '''

# => in nested if loop there is condition inside the condition.

age  = int(input("Enter your age: "))
state = input("Enter your state: ")


if (age > 17):
    print("You are An adult and you are eligible for voting")

    if(state.title() == "Delhi"):
        print("You are eligible for vote")

    else:
        print("You are not from the Delhi")
        
        
else:
    print("You are not eligible for vote")