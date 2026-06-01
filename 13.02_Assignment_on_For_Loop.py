'''Validate 5 Passwords Using 'for loop' '''

'''Problem Statement'''
# Write a python program that :
# 1. uses a for loop tp take 5 passswords as input form the user -- one by one 
# 2. for each password check if 
                # it has at least 8 characters
                #  it contains the @ symobl
# 3. for each password print whether it is VALID or NOT valid 
# ---------------------------------------------------------------------------------

for i in range(1,6):
    password = input(f"Enter password{i}:")
    if len(password) >= 8 and "@" in password:
        print(f"'{password}' is VALID\n")
    else:
        print(f"'{password}'is NOT valid\n")
