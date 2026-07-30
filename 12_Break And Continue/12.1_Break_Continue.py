# break and continue :-

# break : -
# => if the given condition is true in that case we exit from loop immediatly.

for i in range(6):
                    print(i) # 0,1,2,3,4,5


# ---------------------------------------------

for i in range(6):
                    if i == 3:
                                        break
                    print(i)


# i = 0 

# 0 == 3 => False   # 0
# 1 == 3 => False   # 1
# 2 == 3 => False   # 2
# 3 == 3 => False   # Break

# ---------------------------------------------

# ## Continue :- 
# => if the given condition is true , in that case only we skip the current elemnt and move to the next element. 

for i in range(6):
                    if i == 3:
                                        continue
                    print(i)

# i = 0 
# condition => i == 3
# 0 == 3 => False  # 0 
# 1 == 3 => False  # 1
# 2 == 3 => False  # 2 
# 3 == 3 => TRUE  # Continue => ( we skip the current element )

# # 4,5
# # Final Output => 0,1,2,4,5



'''Some exaple of break and continue'''

for i in range(1, 11):
                    if i == 5:
                                        break
                    print(i)




for i in range(1, 11):
                    if i == 5:
                                        continue
                    print(i)



# Question :-
# 1. Print all the numbers from 1 to 20 except 5 and 10 using continue statement.

for i in range(1, 21):
                    if i == 5 or i == 10:
                                        continue
                    print(i)


# 2. Print all the numbers from 1 to 20 until you encounter a number that is divisible by 7 using break statement.

for i in range(1, 21):
                    if i % 7 == 0:
                                        break
                    print(i)


# 3. Print all the even numbers from 1 to 20 using continue statement.

for i in range(1, 21):
                    if i % 2 != 0:
                                        continue
                    print(i)




# 4. Print all the odd numbers from 1 to 20 using continue statement.

for i in range(1, 21):
                    if i % 2 == 0:
                                        continue
                    print(i)  



# 5. Print all the numbers from 1 to 20 until you encounter a number that is greater than 15 using break statement.

for i in range(1, 21):
                    if i > 15:
                                        break
                    print(i)    



# explain