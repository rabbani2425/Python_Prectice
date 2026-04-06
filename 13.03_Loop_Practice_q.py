#1. 1 se 10 tak numbers print karo using for loop

for i in range (1,11):
    print(i)

#2. 1 se 10 tak even numbers print karo

for i in range(1,11,2):
    print(i)


# 3. 10 se 1 tak reverse order me print karo

for i in range(10,0 ,-1):
    print(i)

# 4.1 se 100 tak ka sum nikalo

sum = 0
for i in range(1,101):
    sum += i
print(sum)


# 5. Factorial find karo (e.g., 5! = 120)

factorial = 1
for i in range(1,6):
    factorial *= i
print(factorial)

# 6. Prime number check karo

num = 3
is_prime = True
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        is_prime = False
        break
print(is_prime)

# 7. Fibonacci series print karo (e.g., 0, 1, 1, 2, 3, 5, 8, ...)

a, b = 0, 1
for i in range(10):
    print(a)
    a, b = b, a + b