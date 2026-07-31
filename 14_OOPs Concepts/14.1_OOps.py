'''Class:- its is a collection of instance variable of instance method
it is just like a blue print of object'''

'''Object:- by using this we can access of any property of any class '''

# Note:- methods and function both are same thing.

# ----------------------------------------------------------------------------------------
class Vivek():
    vivek_assets = "VS travels" # class variable
    vivek_stuff = "DUKE byke"

    def print_vivek(self):
        print("This is vivek")

vivek_object = Vivek() # object of class
print(vivek_object.vivek_assets) # access class variable by using object
print(vivek_object.vivek_stuff) # access class variable by using object
vivek_object.print_vivek() # call method by using object


# ----------------------------------------------------------------------------------------------------

class Rohit():
    rohit_acc_number = 1234
    rohit_ifsc_code = "PUMB1676"


    def rohit_info(self):
                        print("all about Rohit")

rohit_obj = Rohit()
print(rohit_obj.rohit_acc_number)
print(rohit_obj.rohit_ifsc_code)
rohit_obj.rohit_info()

# --------------------------------------------------------------------------------------------------

'''there are four pillars in OOPs Programming'''

# 1.Inheritance 
# 2.Polymorphism
# 3.Abstraction
# 4.Encapsulation

# -----------------------------------------------------------------------------------

'''1.Inheritance '''

class Father():
        
        father_first_asset = "VS Travels"
        father_second_asset = "VS Empire"

class Child(Father):

    Child_first_asset = "VIP Travels"
    Child_second_asset = "VIP Empire"

child_obj = Child()

print(child_obj.Child_first_asset)
print(child_obj.father_first_asset)        

# -------------------------------------------------------------------------------------

# Sub class = It inherit super class 
# Super Class = it id inherited by sub class 


# here Father is Super class 

# class father:
#        father_resturent_name = "Chai and Coffee"
#        father_hotel_name = "xyz hotel"

# # Here child is sub calss 

# class child(father):
#         child_foundation_name ="Nirmla Foundation"
#         child_school_name = "xyz kids publlication"
        

