# 1. write a program to print your name 10 times , by using function 

def print_my_name_10_times():
    for i in range(10):
        print("Gulam Rabbani")
print_my_name_10_times()


# 2. write a program to check the given number is even or odd , by using function 
def check_even_odd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(num,"is even number")
    else:
        print(num,"is odd number")

check_even_odd()

# 3. write a prgram , in which you have to create a firstly empty list and insert some value , and check if value is negative then it should be added at the last otherwise it should be added at the random index , by using function 

def insert_value_in_list():
    my_list = []
    value = int(input("Enter a value: "))
    if value < 0:
        my_list.append(value)
    else:
        index = int(input("Enter the index to insert the value: "))
        my_list.insert(index, value)
    print("Updated list: ", my_list)

insert_value_in_list()

# 4. write a program to print your 5 friends name , by using input function and function
def print_friends_names():
    friend_names = []
    for i in range(5):
        name = input("Enter the name of friend {}: ".format(i+1))
        friend_names.append(name)
    print("Friends' names:", friend_names)
print_friends_names()
