'''List:- It can strore multiple items in a single variable and it is ordered and changeable and allows duplicate members.'''

# Creating a list

my_list =[11,12,23,24,25]

list2 = [13,13.4,"Gulam","Rabbani",4,True]

# integer =>11,12,23,24,25
# float => 13.4
# string => "Gulam","Rabbani"
# boolean => True

# () => Parenthesis
# {} => Curly Braces
# [] => Square Brackets

# List is defined by using Square Brackets
'''List positive and negative Indexing'''

#         0  1  2  3
my_list =[11,12,24,25] 
print(my_list)
print(my_list[0]) # 11
print(my_list[1]) # 12
print(my_list[2]) # 24
print(my_list[3]) # 25

# --------------------------------------------------------------
#       -6  -5    -4      -3      -2  -1 
list2 = [13,13.4,"Gulam","Rabbani",4,True]

print(list2[-6]) # 13
print(list2[-5]) # 13.4
print(list2[-4]) # Gulam
print(list2[-3]) # Rabbani
print(list2[-2]) # 4
print(list2[-1]) # True
# -----------------------------------------------------------------
'''List Slicing'''

list3 = ["Gulam","Rabbani","Fardin","Harsit","Ashish","Vivek"]
print(list3[0:3]) # ["Gulam","Rabbani","Fardin"]
print(list3[1:4]) # ["Rabbani","Fardin","Harsit"]
print(list3[:3])  # ["Gulam","Rabbani","Fardin"]
print(list3[3:6]) # ["Harsit","Ashish","Vivek"]
print(list3[3:])  # ["Harsit","Ashish","Vivek"]

#        0  1   2  3  4  5   6     7        8
list3 = [22,33,44,55,66,77,88.8, "Vicky", "abhi"]

print(list3[3]) # 55
print(list3[7: ])
print(list3[4: 7])


