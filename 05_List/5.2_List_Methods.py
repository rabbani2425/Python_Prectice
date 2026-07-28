'''List Methods in Python:'''
# 1.append() => it is used to add a single element at the end of list.

my_listt = [10,20,30,40,50,60]
print("before applying any method: ", my_listt)
my_listt.append(66)
print("after applying any operation: ", my_listt)
# -------------------------------------------------------------------

# 2.extend() => it is used to add multiple elements at the end of list.

my_listt = [10,20,30,40,50,60]
print("before applying any method: ", my_listt)

my_listt.extend([66,77])
print("after applying any operation: ", my_listt)
# -------------------------------------------------------------------

# 3.insert() => it is used to add an element at a specific index.
my_listt = [10,20,30,40,50,60]
print("before applying any method: ", my_listt)
my_listt.insert(2, 25)
print("after applying any operation: ", my_listt)
# -------------------------------------------------------------------

# 4.remove() => it is used to remove the mantioned element.
my_listt = [10,20,30,40,50,60]
print("before applying any method: ", my_listt)
my_listt.remove(30)
print("after applying any operation: ", my_listt)
# -------------------------------------------------------------------

# 5.pop() =>by default it removes the last element ,otherwise it removes the specified index element .
my_listt = [10,20,30,40,50,60]
print("before applying any method: ", my_listt)

my_listt.pop()
print("after applying any operation: ", my_listt)

my_listt = [10,20,30,40,50,60]
print("before applying any method: ", my_listt)

my_listt.pop(1)
print("after applying any operation: ", my_listt)
# -------------------------------------------------------------------

# 6.index() => it returns the index of the mentioned element.

my_listt = [10,20,30,40,50,60]
print("before applying any method: ", my_listt)
print(my_listt.index(20)) # 1
print("after applying any operation: ", my_listt)


my_listt = [10,20,30,40,50,60]
print("before applying any method: ", my_listt)
my_listt.index(20)
print("after applying any operation: ", my_listt)


my_listt = [10,20,30,20,20,20,40,50,60]
print("before applying any method: ", my_listt)
print(my_listt.count(20))
print("after applying any operation: ", my_listt)
# -------------------------------------------------------------------

# 7.reverse()

my_listt = [10,20,30,20,20,20,40,50,60]
print("before applying any method: ", my_listt)
my_listt.reverse()
print("after applying any operation: ", my_listt)
# -------------------------------------------------------------------

# 8. sorted() => by default it arranges elements in ascending ordr.

my_listt = [10,20,30,2,20,20,4,50,6]
print("before applying any method: ", my_listt)
my_listt.sort()
print("after applying any operation: ", my_listt)
# -------------------------------------------------------------------

# 9.descending order 

my_listt = [10,20,30,2,20,20,4,50,6]
print("before applying any method: ", my_listt)
my_listt.sort(reverse=True)
print("after applying any operation: ", my_listt)
# -----------------------------------------------------------------------

# 10.copy() :-

my_listt = [10,20,30,20,20,20,40,50,60]
print("before applying any method: ", my_listt)

my_listt2 = my_listt.copy()
print("after applying any operation: ", my_listt2)