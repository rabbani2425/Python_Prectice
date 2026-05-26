
# Function :- 

# => it is a block of code . 
# => it can increase our code reusabaility. 
# => it can save our time . 
# => it can increase code readablity.

# function definition 

def print_all_student_name():
                    print("Gulaam")
                    print("Neha")
                    print("Palak")
                    print("Rohit")

# function call 
print_all_student_name()

print("second time ")

print_all_student_name()


# ------------------------------------ 

a = 100

b = 50

if a > b:
                    print("a is greater ")
else:
                    print("b is greater")

# --------------------------------------------------------

#       >     => greater than
#       <     => less than


# ---------------------------------------------- 

a = int(input("enter the value of a : "))

b = int(input("enter the value of b : "))

if a > b:
                    print("a is greater ")
else:
                    print("b is greater")

# ---------------------------------------------------------- 


def compare_two_variable(a,b):
                    if a > b:
                                        print("a is greater")
                    else: 
                                        print("b is greater")

compare_two_variable(222,444)


'''# types of funciton :-'''

# 1. Function with parameter 
#    a. Postional Argument
#    b. Default Argument 
# 2. Function without parameter 



# 1. Function with parameter 
#    a. Postional Argument

# example :-

def sum_of_two_variables(a,b):
                    print("the sum is : ", a + b)

sum_of_two_variables(100,190)



# 1. Function with parameter 
#    b. Default Argument 



# example :-

def sum_of_two_variables(a,b = 20):
                    print("the sum is : ", a + b)

sum_of_two_variables(100) 
sum_of_two_variables(100, 300)


# 2. Function without parameter 

# example :-

def print_my_name():
                    print("Shashant")

print_my_name()


# 1. write a program to print your name 10 times , by using function 
# 2. write a program to check the given number is even or odd , by using function 
# 3. write a prgram , in which you have to create a firstly empty list and insert some value , and check if value is negative then it should be added at the last otherwise it should be added at the random index , by using function 

# 4. write a program to print your 5 friends name , by using input function and function