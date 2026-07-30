'''Assignment on Nested IF'''

'''1.Login and Role access '''
# Write a Python program that performs the folling steps:
            # 1.Ask the user to enter a username.
            # 2.Ask the user to enter a password.
            # 3.if the username is "admin":
                                        # the check if the password is "admin123":
                                        # if both are correct, print:"Welcome, Admin!"
                                        
                                        #  else,print:"Incorrect Password."  

            # 4.if the username is not "admin":
                                    # print,"Invalid username."
# ----------------------------------------------------------------------------------------

username = input("Enter your username:")
password = input("Enter your Password:")

if username == "admin":
    if password == "admin123":
        print("Welcome, Admin!")
    else:
        print("Incorrect Password.")
else:
    print("Invaild username.")

# ----------------------------------------------------------------------------------------
'''2. Age + License Check '''
# Ask for user age:
# if age >= 18:
            # ask if they have a license (yes or no)
                                    # if yes --> print"You can drive"
                                    # if no --> print "Get a license first."
# Else --> print, "You are underage"
# ----------------------------------------------------------------------------------------

age = int(input("Enter your age:"))
if age >= 18:
    license_status = input("Do you have a license?(yes / no ):")
    if license_status.lower() == "yes":
        print("You can drive.")
    else:
        print("Get a license first.")
else:
    print("You are underage.")

# ----------------------------------------------------------------------------------------

'''3. Simple ATM Simulator'''

# Ask for pin(use 2425 as correct pin)
# if pin is correct :
            # Ask for withdrawal amount 
            # if ammount <= 10000 --> print "Transaction Successful"
            # Else --> prrint "Limit Exceeded"
# else --> print "Wrong Pin"

pin = int(input("Enter your 4-digit PIN:"))
if pin == 2425:
    amount = int(input("Enter withdrawal amount:"))
    if amount <= 10000:
        print("Transaction Successful")
    else:
        print("Limit Exceeded")
else:
    print("Wrong Pin")