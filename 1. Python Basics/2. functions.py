# ....
def greeting(name): #a function takes parameters. Here, "name" is a parameter of the greeting() function 
    print("Welcome, " + name)
greeting("Kay")
greeting("Cameron")

def greeting(name, department): # 2 parameters: "name" and "department"
    print("Welcome, " + name)
    print("You are part of " + department)
greeting("Blake", "Software engineering")
greeting("Ellis", "Software engineering")

# Parameters vs Arguments
# PARAMETERS are the objects listed inside parentheses in the function definition, while ARGUMENTS are the values passed to the
#..to the function when it is called.
# In the examples above, "name" and "department" are parameters, while "Kay" and "Software Engineering" are arguments.
# NB: Both words are sometimes used interchangeably



#**********************RETURNING VALUES********************
def area_triangle(base, height):
    return base*height/2
area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
hrs, mins, rem_secs = convert_seconds(5000) #When a function returns muliple values, these values MUST be stored in separate variables
print(hrs, mins, rem_secs)
print("5000 seconds equals " + str(hrs) + "hrs, " + str(mins) + "mins, and " + str(rem_secs) + " secs") #a task like this is possible
#..because the values are stored in separate variables 

def greeting(name):
    print("Welcome, " + name)
result = greeting("Christine")
print(result)


#**********************THE PRINCIPLES OF CODE REUSE********************
name = "Kay"
number = len(name) * 9 # this line is duplicated in the second code block below
print("Hello " + name + ". Your lucky number is " + str(number)) #this line is also duplicated in the code block below

name = "Cameron"
number = len(name) * 9
print("Hello " + name + ". Your lucky number is " + str(number))

#Functions can be very helpful in avoiding duplication:
def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))
lucky_number("Kay")
lucky_number("Cameron")


#**********************CODE STYLE********************
#It's good practice is to make codes self-documenting (i.e., well-written in a way that's readable and doesn't conceal its intent)
# The following code isn't explicit enough as to what it does
def calculate(d):
    q = 3.14
    z = q * (d ** 2)
    print(z)
calculate(5) #Output is 78.5

#Contrast with the following:
def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)
circle_area(5) #Output is 78.5
# Although both codes are performing the same task, the second has been refactored (i.e., rewritten to make the intent more
#..understandable. The code is simply writtent to be more explanatory without changing its functonality). Thus, this code is
#..self-documenting




#*****************------------PRACTICE QUIZ------------------***********************
# 1. This function converts miles to kilometers (km).
#   Complete the function to return the result of the conversion
#   Call the function to convert the trip distance from miles to kilometers
#   Fill in the blank to print the result of the conversion
#   Calculate the round-trip in kilometers by doubling the result, and fill in the blank to print the result
# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km
my_trip_miles = 55
# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)
# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))
# 4) Calculate the round-trip in kilometers by doubling the result, and fill in the blank to print the result
print("The round-trip in kilometers is " + str(my_trip_km * 2))


#2. Let's revisit our lucky_number function. We want to change it, so that instead of printing the message, it returns the 
#..message. This way, the calling line can print the message, or do something else with it if needed. Fill in the blanks to 
#..complete the code to make it work.
def lucky_number(name):
  number = len(name) * 9
  output = "Hello " + name + ". Your lucky number is " + str(number)
  return output
print(lucky_number("Kay"))
print(lucky_number("Cameron"))
