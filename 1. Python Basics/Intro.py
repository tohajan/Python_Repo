# Skill 1: using the print() function
print("Hello, World!")

# Syntax for printing a string of text
print("I love Python!")

# Syntax for printing numeric values
print(360)
print(32*45)

# Syntax for printing the value of a variable
value = 8*6
print(value)


# Skill 2: Using arithmetic operators, with a focus on exponents
# Multiplication, division, addition, and subtraction
print(3*8/2+5-1)
 
# Exponents
print(4**6) # Syntax means 4 to the power of 6
print(4**2) # To square a number
print(4**3) # To cube a number
print(4**0.5) # To find the square root of a number

# To calculate how many different possible combinations can be formed using a set of "x" characters with each character in "x"
# having "y" number of possible values, you will need to use an exponent for the calculation:
x = 4
y = 26
print(y**x)

print(7+8) #prints out "15"
print("hello "+ "world") #prints "hello world"
print(7+"8") #TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(type("a")) #prints out "<class 'str'>"
print(type(2)) #prints out "<class 'int'>"
print(type(2.5)) #prints out "<class 'float'>"



#****************VARIABLE ANNOTATION******************************
name: str="Betty" #the "str" helps to label (annotate) the variable name, i.e., hint that the variable should hold a string value.
age: int=34 #likewise, "int" hints that the age variable should hold an integer type value

#However, Python is flexible and doesn't require a programmer to declare variable types. That is, the type of variable can change over 
#..time as new values are assigned to it. This phenomenon is known as dynamic typing (allows programmers to write code more quickly and 
#..offers flexibility because you don’t have to explicitly declare the type of variable)

#*****************
print(7+8.5)
print("a"+"b"+"c")
print("This " + "is " + "pretty " + "neat!")
base = 6
height = 3
area = (base*height)/2
print("The area of the triangle is: " + str(area)) #the str() function here converts the numerical object to a string

# PRACTICE QUESTION
#In this scenario, we have a directory with 5 files in it. Each file has a different size: 2048, 4357, 97658, 125, and 8. Fill in the 
#..blanks to calculate the average file size by having Python add all the values for you, and then set the files variable to the number 
#..of files. Finally, output a message saying "The average size is: " followed by the resulting number. Remember to use the str() function 
#..to convert the number into a string. 
total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total / files
print("The average size is: " + str(average))