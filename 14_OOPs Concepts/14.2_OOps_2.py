'''Types of inheritance:'''

# Single Inheritance
# Multiple Inheritance
# Multilevel Inheritance
# Hierarchical Inheritance
# Hybrid Inheritance

# ----------------------------------------------------------------------------------------------------

'''Single Inheritace:- In this case a sub class inherits only one super class'''

class father:
       father_resturent_name = "Chai and Coffee"
       father_hotel_name = "xyz hotel"


class child(father):
        child_foundation_name ="Nirmla Foundation"
        child_school_name = "xyz kids publlication"

child_obj = child()
print(child_obj.father_resturent_name)
print(child_obj.child_foundation_name)

# ----------------------------------------------------------------------------------------------

'''Multiple Inheritance:- In this case one sub class inherits multiple super class'''

class Grandfather():
        grandfather_restaurant_name = "Grand tea wala"
        grandfather_hotel_name = "Grand hotel"

class father:
       father_resturent_name = "Chai and Coffee"
       father_hotel_name = "xyz hotel"

class child(Grandfather,father):
        child_foundation_name ="Nirmla Foundation"
        child_school_name = "xyz kids publlication"


child_obj = child()
print(child_obj.father_resturent_name)  #Chai and Coffee
print(child_obj.child_foundation_name) #Nirmla Foundation
print(child_obj.grandfather_restaurant_name) #Grand tea wala

# --------------------------------------------------------------------------------------------------------------------

'''Multilevel Inheritance'''

class GrandFather():
                    grandfather_first_asset = "Grand Travels"
                    grandfather_second_asset = "Grand Empire"


class Father(GrandFather):
                    father_first_asset = "VS Travels"
                    father_second_asset = "VS Empire"


class Child(Father):
                    Child_first_asset = "VIP Travels"
                    Child_second_asset = "VIP EMpire"

child_obj = Child()

print(child_obj.Child_first_assets) #Output=>   VIP Travels
print(child_obj.father_first_asset)  #Output=>  VS Travels

father_obj = Father()

print(father_obj.grandfather_first_asset)  #Output=>  Grand Travels

# -----------------------------------------------------------------------------------------------------------------------

'''Encapsulation:- In this case a sub class inherits only one super class'''

class Vivek_info():
        vivek_bank_name = "SBI"
        __vivek_bank_account_number = "1234567890"  #Private variable
        vivekDebitCardCVV = "123"  #Public variable

vivek_obj = Vivek_info()
print(vivek_obj.vivek_bank_name)  #Output=> SBI
print(vivek_obj.vivekDebitCardCVV)  #Output=> 123 

# ---------------------------------------------------------------------------------------------------------------------------


# Note:-
#          so there are three types of access specifier. 
#  a. Public 
#  b. Protected
#  c. Private



#  1. We can make any variable protected by using single underscore ("_")
#  Example : _vivekBankAccountNumber = "1234567898767"

#  2. We can make any variable private by using Double underscore ("__")

#  Example => __AtmNumber 

class Gulam_info():
        gulam_bank_name = "PNB"
        _gulam_bank_account_number = "0987654321"  #Protected variable
        __gulam_atm_number = "1111"  #Private variable


my_obj = Gulam_info()
print(my_obj.gulam_bank_name)  #Output=> PNB
print(my_obj._gulam_bank_account_number)  #Output=> 0987654321
print(my_obj._Gulam_info__gulam_atm_number)  #Output=> 1111

# ---------------------------------------------------------------------------------------------------------------------------

'''Polymorphism:- In this case a sub class inherits only one super class'''


# poly = more 
# phism = forms

# many forms

# there are 2 types of polymorphism in python

#  1. Compile time Polymorphism OR Function overloading
#  2. Runtime polymorphism OR Function Overriding


# Function overloading


class Vivek():
      def assets(self):
            print(" Vivek Assets")

class Aditya():
      def assets(self):
            print("Aditya assets")

vivek_obj = Vivek()
aditya_obj = Aditya()

vivek_obj.assets()
aditya_obj.assets()


'''Function Overriding'''


class Parent():
      def assets(self):
            print("Parent Assets")

class Child(Parent):
      def assets(self):
            print("Child Assets")

child_obj = Child()
child_obj.assets()

# -------------------------------------------------------------------------------------------

'''Abstraction:- In this case a sub class inherits only one super class'''


from abc import ABC, abstractmethod

class secure_class():

         @abstractmethod
         def secure_fxn(self):
             pass

class secure_child_class(secure_class):

     def secure_fxn(self):
         print(" it's the confidential data , please keep it secure")

secure_child_class_object = secure_child_class()

secure_child_class_object.secure_fxn()

# ------------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod

class secure_class():  # this is abstract class 

        @abstractmethod
        def secure_fxn(self):  ## this is abstract method
            pass

        def regular_fxn(self):  ## this is regular method
             print(" this is regular method")

class secure_child_class(secure_class):

    def secure_fxn(self):
        print(" it's the confidential data , please keep it secure")

secure_child_class_object = secure_child_class()

secure_child_class_object.secure_fxn()
secure_child_class_object.regular_fxn()
secure_child_class_object = secure_child_class()

secure_child_class_object.secure_fxn()
secure_child_class_object.regular_fxn()

