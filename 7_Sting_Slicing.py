'''String Slicing :- Slicing ka matlb hota h striing ke andar se kuch part ko nikalna and index ke help se '''

# For 2 perameters String slicing:

# First perameters = Stating Point.
# Second perameters = Ending Point.

# Some's rules:-

# 1). by defult(pahle se tay hai) Stating point will be always 0.
# 2). by defult Ending point will be always Excluded.
# 3). by defult Ending point will be last index.

# P r o g r a m m i n g
# 0 1 2 3 4 5 6 7 8 9 10
'''Example 1'''
words = "Programming" # mujhe is me se "Pro" nikalna h
print(words)
print("Slicing:",words[0:3])

#  yaha pe 
# 0=> Staing Point 
# 3=> Ending Point but (3 include nahi hota)/ 0th to 2th
# OUTPUT :- Pro

'''Example 2 '''
#  0 1 2 3 4 5 6
#  r a b b a n i

# my_name = "rabbani" # is me mujhe "abb" and "abban" ko Slicing karna hai
# print("1).Slicing:",my_name[1:4])
#  1=> Staing point
#  4=> Ending point but (4 include nahi hoga) 1th and 

# OUTPUT:=abb

# print("2).Slicing:",my_name[1:6])

'''Example 3'''

# 0 1 2 3 4 5 6 7 8 9
# j a v a s c r i p t

my_string = "javascript" # mujhe is me "javas" ko slicing karna hai
print("Slicing:",my_string[ :5])

# Stating point :- 0
# Ending Point :- 5 (not included by 5 position)

# OUTPUT= javas
''''-------------------------------------------------------------------'''

# 0 1 2 3 4 5 6 7 8 9
# j a v a s c r i p t

# my_string = "javascript" # mujhe is me "jav" chor ka baki sab ka slicing karna hai
# print("Slicing:",my_string[3: ])

# Stating point => 3
# Ending point => Last index
# OPUTPUT = 3 to 9 => ascript
'''-------------------------------------------------------'''

# 0 1 2 3 4 5 6 7 8 9
# j a v a s c r i p t

my_string = "javascript" # mujhe is me ab "javascript" ka slicing karna hai
print("Slicing:",my_string[:])

# Stating point => 0
# Ending Point => Last Index
# OUTPUT = javascript


