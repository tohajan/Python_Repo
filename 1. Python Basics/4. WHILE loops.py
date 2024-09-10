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
while my_variable < 10:
    print("Hello")
    my_variable += 1
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

while True:
    do_something_cool()
    if user_requested_to_stop():
        break #this breaks an infinite loop

#PRACTICE
#The following code causes an infinite loop. Can you figure out what’s missing and how to fix it?
def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
		n+=1 #THIS LINE IS THE FIX. IT WASN'T INCLUDED IN THE ORIGINAL CODE.
print_range(1, 5)