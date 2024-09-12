#---- Introduction-----
#While loops instruct your computer to continuously execute your code based on the value of a condition. It's
#..similar to the IF statement except the body of a WHILE block can be executed multiple times instead of just once.

x =   0 #initializing
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))

# More examples
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
attempts(5)


#*********************WHY INITIALIZING VARIABLES MATTERS**********************
# while my_variable < 10:
#     print("Hello")
#     my_variable += 1
#The above code returns an error because my_variable is not defined/initialized. The following fixes the issue:
my_variable = 5
while my_variable < 10:
    print("Hello")
    my_variable += 1
#The code now prints "Hello" 5 times, starting with when my_variable has a value of 5 (the initialized value) up until a value of 9.

x = 1
sum = 0
while x < 10:
    sum = sum + x
    x = x + 1
# x and sum are correctly initialized in the above code. However, there's an error in the following code which may not be flagged
#..in the output: x is not initialized. Thus, it will retain the final value of x from the code exceuted above (i.e., 10), which
#..isn't what is intended
product = 1
while x < 10:
    product = product * x
    x = x + 1
print(sum, product) # output is "45 1". No error message.

#Now, let's reinitialize x:
product = 1
x = 1
while x < 10:
    product = product * x
    x = x + 1
print(sum, product) # output is now "45 362880".

#A similar problem is seen below:
def count_down(start_number):
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")
count_down(3)
#This code returns the error message: "UnboundLocalError: local variable 'current' referenced before assignment"

#The code is fixed by initializing 'current':
def count_down(start_number):
  current=3
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")
count_down(3)


#*********************INFINITE LOOPS AND HOW TO BREAK THEM**********************
#An infinite loop is a loop that keeps executing and never stops
while x % 2 == 0:
    x = x / 2
#For this code, if x is initialized as 0, the loop will continue indefinitely. This can be avoided in several ways. Two
#..examples are given next:
if x != 0: #Here, the loop is executed only when x is not equal to 0
    while x % 2 == 0:
        x = x / 2

while x != 0 and x % 2 == 0: #Here, the loop is exceuted only if the two defined conditions are met
    x = x / 2

# while True:
#     do_something_cool()
#     if user_requested_to_stop():
#         break #this breaks an infinite loop

#PRACTICE
#The following code causes an infinite loop. Can you figure out what’s missing and how to fix it?
def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
		n+=1 #THIS LINE IS THE FIX. IT WASN'T INCLUDED IN THE ORIGINAL CODE.
print_range(1, 5)



# *************** PRACTICE QUIZ**********************
#1. The following code contains an infinite loop, meaning the Python interpreter does not know when to exit the loop once the task is 
#..complete. To solve the problem, you will need to:
#       Find the error in the code
#       Fix the while loop so there is an exit condition

# def is_power_of_two(number):
#   # This while loop checks if the "number" can be divided by two without leaving a remainder. How can you change the while loop to
#   # avoid a Python ZeroDivisionError?
#   while number % 2 == 0:
#     number = number / 2
#   # If after dividing by 2 "number" equals 1, then "number" is a power of 2.
#   if number == 1:
#     return True
#   return False
# # Calls to the function
# print(is_power_of_two(0)) # Should be False
# print(is_power_of_two(1)) # Should be True
# print(is_power_of_two(8)) # Should be True
# print(is_power_of_two(9)) # Should be False

# SOLUTION:
def is_power_of_two(number):
  if number == 0:
    return False
  if number == 1:
    return True
  elif number > 1:
    while number % 2 == 0:
      number = number / 2
      if number == 1:
        return True
    return False
# Calls to the function
print(is_power_of_two(0)) # False
print(is_power_of_two(1)) # True
print(is_power_of_two(8)) # True
print(is_power_of_two(9)) # False


# #2. Write a function that takes an argument n and returns the sum of integers from 1 to n. For example, if n=5, your 
# #..function should add up 1+2+3+4+5 and return 15. If n is less than 1, just return 0. Use a while loop to calculate this sum. 
# def sum_of_integers(n):
#   if n < 1:
#     return 0
#   i = 1
#   sum = ___
#   while ___:
#     sum = sum + i
#     i = ___
#   return sum
# print(sum_of_integers(3))  # should print 6
# print(sum_of_integers(4))  # should print 10
# print(sum_of_integers(5))  # should print 15

#SOLUTION:
def sum_of_integers(n):
  if n < 1:
    return 0
  i = 1
  sum = 0
  while i <= n:
    sum = sum + i
    i = i+1
  return sum
print(sum_of_integers(3))  # 6
print(sum_of_integers(4))  # 10
print(sum_of_integers(5))  # 15


#3. Fill in the blanks to complete the function, which should output a multiplication table. The function accepts a 
#..variable “number” through its parameters. This “number” variable should be multiplied by the numbers 1 through 5, and 
#..printed in a format similar to “1x6=6” (“number” x “multiplier” = “result”). The code should also limit the “result” 
#..to not exceed 25. To satisfy these conditions, you will need to:
#       Initialize the “multiplier" variable with the starting value
#       Complete the while loop condition
#       Add an exit point for the loop
#       Increment the “multiplier" variable inside the while loop
# def multiplication_table(number):
#     # Initialize the appropriate variable
#     ___ = ___
#     # Complete the while loop condition.
#     while ___:
#         result = number * multiplier 
#         if  result > 25:
#             # Enter the action to take if the result > 25
#             ___
#         print(str(number) + "x" + str(multiplier) + "=" + str(result))
#         # Increment the appropriate variable
#         ___ += 1
# multiplication_table(3) 
# # Should print: 
# # 3x1=3 
# # 3x2=6 
# # 3x3=9 
# # 3x4=12 
# # 3x5=15
# multiplication_table(5) 
# # Should print: 
# # 5x1=5
# # 5x2=10
# # 5x3=15
# # 5x4=20
# # 5x5=25
# multiplication_table(8) 
# # Should print:
# # 8x1=8
# # 8x2=16
# # 8x3=24

# SOLUTION
def multiplication_table(number):
    multiplier = 1
    while multiplier <= 5:
        result = number * multiplier 
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1
multiplication_table(3) # prints: 
#                               3x1=3 
#                               3x2=6 
#                               3x3=9 
#                               3x4=12 
#                               3x5=15

multiplication_table(5) # prints: 
#                               5x1=5
#                               5x2=10
#                               5x3=15
#                               5x4=20
#                               5x5=25

multiplication_table(8) # prints:
#                               8x1=8
#                               8x2=16
#                               8x3=24