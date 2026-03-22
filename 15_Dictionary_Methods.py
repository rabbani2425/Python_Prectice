'''Dictionary Methods in Python:-'''

# 1. key()
# 2. values()
# 3. items()
# 4. get()
# 5. update()
# 6. pop()
# 7. popitem()
# 8. clear()

student = {
    "name" : "Rabbani",   # here, name is key and Rudra is Value
    "age" : 20, 
    "city" : "Delhi",
    "course" : "Python"
}

# 1. keys() => it is used to get all the keys of a dictionary.

print(student.keys()) # dict_keys(['name', 'age', 'city', 'course'])
# ------------------------------------------------------------------------------------------

# 2. values() => it is used to get all the values of a dictionary.

print(student.values()) # dict_values(['Rabbani', 20, 'Delhi', 'Python'])
# ------------------------------------------------------------------------------------------


# 3. items() => it is used to get all the key value pairs of a dictionary.

print(student.items()) # dict_items([('name', 'Rabbani'), ('age', 20), ('city', 'Delhi'), ('course', 'Python')])
# ------------------------------------------------------------------------------------------

# 4. get() => it is used to get the value of a key.
print(student.get("name")) # Rabbani
print(student.get("age")) # 20
print(student.get("city")) # Delhi
print(student.get("course")) # Python
# ------------------------------------------------------------------------------------------    
# 5. update() => it is used to update the value of a key.

student.update({"name" : "Gulam"}) # Rabbani = Gulam
student.update({"age" : 21})       # 20 = 21
student.update({"city" : "Biahr"}) # Delhi = Bihar
student.update({"course" : "Java"}) # Python = Java
print(student) # {'name': 'Gulam', 'age': 21, 'city': 'Biahr', 'course': 'Java'}
# ------------------------------------------------------------------------------------------
# 6. pop() => it is used to remove a key value pair from a dictionary.

student.pop("name") # it will remove the key value pair of name
print(student) # {'age': 21, 'city': 'Biahr', 'course': 'Java'}
# ------------------------------------------------------------------------------------------
# 7. popitem() => it is used to remove the last key value pair from a dictionary.

student.popitem() # it will remove the last key value pair of course
print(student) # {'age': 21, 'city': 'Biahr'}
# ------------------------------------------------------------------------------------------
# 8. clear() => it is used to remove all the key value pairs from a

student.clear() # it will remove all the key value pairs from a dictionary
print(student) # {}