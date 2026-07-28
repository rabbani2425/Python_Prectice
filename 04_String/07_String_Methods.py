'''String Methods'''

'''1).upper():-It converts all characters in uppercase or capital letters'''

# EXAMPLE

my_string = "python is a programming lenguge."
print("Befor any operation:",my_string)
print("After any operation:",my_string.upper())
# -------------------------------------------------------------------------
'''2).lower():-It converts all characters in lowercase or small letters'''

# EXAMPLE

my_string = "PYTHON IS A PROGRAMMING LENGUGE."
print("Befor any operation:",my_string)
print("After any operation:",my_string.lower())
# --------------------------------------------------------------------------
'''3).capitalize():- it converts the first character of first word in uppercase or capital letter'''
# EXAMPLE

my_string = "python."
print("Befor any operation:",my_string)
print("After any operation:",my_string.capitalize())
# --------------------------------------------------------------------------
'''4).titel():- It converts the first letter of every word into a capital letter.'''

# EXAMPLE

my_string = "python is a programming lenguge."
print("Befor any operation:",my_string)
print("After any operation:",my_string.title())
# --------------------------------------------------------------------------
'''5).strip():-It removers the extra space'''

# EXMPLE

my_string = "    'python is a programming lenguge'      "
print("Befor any operation:",my_string)
print("After any operation:",my_string.strip())
#---------------------------------------------------------------------------
'''6).replace():- It replace a word or character with another word or charcter '''

# EXAMPLE

my_string = "Python is a Programming Lenguge."
print("Befor any operation:",my_string)
print("After any operation:",my_string.replace("Python","Java"))
#---------------------------------------------------------------------------
'''7).split():-it Split a string into a list'''

# EXMPLE
my_string = "Python is a Programming Lenguge."
print("Befor any operation:",my_string)
print("After any operation:",my_string.split())
#---------------------------------------------------------------------------
'''8).find():-Find the first occurence position of character or word'''

# EXAMPLE

my_string = "Programming."
print("Befor any operation:",my_string)
print("After any operation:",my_string.find("g"))
#---------------------------------------------------------------------------
'''9).count():- it count how many times character or a word appears in my string.'''

# EXMPLE

my_string = "Python is a Programming Lenguge."
print("Befor any operation:",my_string)
print("After any operation:",my_string.count("g"))
print("After any operation:",my_string.count("o"))
print("After any operation:",my_string.count("m"))
print("After any operation:",my_string.count("m"))
print("After any operation:",my_string.count(" "))
# --------------------------------------------------------------------------
'''10).starswith():-checks if the string starts with specific word'''

# EXAMPLE

my_string = "Python is a Programming Lenguge."
print("Befor any operation:",my_string)
print("After any operation:",my_string.startswith("lenguge"))
print("After any operation:",my_string.startswith("Python"))
# ------------------------------------------------------------------------------

'''11).endswith():-checks if the string ends with specific word'''

#EXAMPLE

my_string = "Python is a Programming Lenguge"
print("Befor any operation:",my_string)
print("After any operation:",my_string.endswith("Lenguge"))
print("After any operation:",my_string.endswith("Python"))