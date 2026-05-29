# Python Assignment:use of input() function

'''Part A: Basic Employee Data Entry '''
# Write a python program that asks the user to enter the following employee details:

                # Name 
                # Employee ID
                # Department
                # Monthly Salary(in ₹)

# name = input("Enter employee name:")
# emp_id = input("Enter employee ID:")
# departement = input("Enter departement name:")
# salary = float(input("Enter monthly salary(₹):"))

# print("\nEmployee Profile:")
# print("Name",name)
# print("Employee ID",emp_id)
# print("Department:",departement)
# print("Monthly Salary:₹",salary)

# ------------------------------------------------------------

'''Part B: Salary Hike Calculator '''

# Extend the above program to also ask:
            # Hike parcentage(e.g, 10)

# then calculate the new salary after the hike and print:
            # Expected Salary After 10 % hike:66000.0
# formula tip use :new salary = salary +(salary * hike _parcent/100)

# hike_parcent = float(input("Enter hike percentage:")) # e.g, 10
# salary = float(input("Enter monthly salary(₹):"))
# # Calculate new salary after this 
# new_salary= salary +(salary * hike_parcent/100)
# print("\nExpected Salary After", hike_parcent, "%Hike:₹",new_salary)

# -----------------------------------------------------------------------
'''Part C : client Data Collenction (for CRM entry)'''
# Ask the used to enter
        # Client Name 
        # Project Name 
        # Projecct Budget 
        # Deadline (in DD/MM/YYYY formate )

# client_name = input("Enter client name:")
# project_name = input("Enter project name:")
# project_budget = float(input("Enter project budget:₹"))
# deadline = input("Enter deadline(DD/MM/YYYY):")

# print("\nClient Project Summary:")
# print("Client Name:",client_name)
# print("Project Name:",project_name)
# print("Project Budget:",project_budget)
# print("Deadline:",deadline)

# ----------------------------------------------------

'''Part D: Feadback form '''
# Ask the user to provide 
        # Full name 
        # Email
        # Rate your training experience (out of 5)
        # write the short comment 

full_name = input("Enter your Full Name:")
email = input("Enter your email:")
rating = int(input("Rate the training(out of 5):"))
comment = input("Write a short comment about the session:")

print("\nThank you,",full_name,"for your feadback!")
print("Your rating:",rating,"/5")
print("eamil:",email)
print("Comment:",comment)


