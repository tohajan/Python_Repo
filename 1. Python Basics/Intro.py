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



#****************TYPE ANNOTATION FOR VARIABLES******************************
name: str="Betty" #the "str" helps to label (annotate) the variable name, i.e., hint that the variable should hold a string value.
age: int=34 #likewise, "int" hints that the age variable should hold an integer type value

#However, Python is flexible and doesn't require a programmer to declare variable types. That is, the type of variable can change over 
#..time as new values are assigned to it. This phenomenon is known as dynamic typing (allows programmers to write code more quickly and 
#..offers flexibility because you don’t have to explicitly declare the type of variable)

# More on variable annotation...
#Type annotations are optional in Python. They can be very helpful, though, because they make code easier to read. Annotations 
# ..make the variable types clear to those reading the code. They can also help you catch errors during compilation. In the example 
# ..below, we are using the typing module to annotate the different types of variables.
import typing
# Define a variable of type str
z: str = "Hello, world!"
# Define a variable of type int
x: int = 10
# Define a variable of type float
y: float = 1.23
# Define a variable of type list
list_of_numbers: typing.List[int] = [1, 2, 3]
# Define a variable of type tuple
tuple_of_numbers: typing.Tuple[int, int, int] = (1, 2, 3)
# Define a variable of type dict
dictionary: typing.Dict[str, int] = {"key1": 1, "key2": 2}
# Define a variable of type set
set_of_numbers: typing.Set[int] = {1, 2, 3}


#*****************
print(7+8.5)
print("a"+"b"+"c")
print("This " + "is " + "pretty " + "neat!")
base = 6
height = 3
area = (base*height)/2
print("The area of the triangle is: " + str(area)) #the str() function here converts the numerical object to a string

# EXAMPLES
#1. In this scenario, we have a directory with 5 files in it. Each file has a different size: 2048, 4357, 97658, 125, and 8. Fill in the 
#..blanks to calculate the average file size by having Python add all the values for you, and then set the files variable to the number 
#..of files. Finally, output a message saying "The average size is: " followed by the resulting number. Remember to use the str() function 
#..to convert the number into a string. 
total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total / files
print("The average size is: " + str(average))

#2. (Skillset: 
#       -Output multiple string variables on a single line to form a sentence
#       -Use the plus (+) connector or a comma to connect strings in a print() function
#       -Create spaces between variables in  a print() function)
# The following 5 lines assign strings to a list of variables.
salutation = "Dr."
first_name = "Prisha"
middle_name = "Jai"
last_name = "Agarwal"
suffix = "Ph.D."
 
print(salutation + " " + first_name + " " + middle_name + " " + last_name + ", " + suffix) 
# The comma as a string ", " adds the conventional use of a comma plus a 
# space to separate the last name from the suffix.
 
# Alternatively, you could use commas in place of the + connector:
print(salutation, first_name, middle_name, last_name,",", suffix)
# However, this produces a space before a comma within a string.



#**********************----------PRACTICE QUIZ----------**************************
#1. In this scenario, two friends are eating dinner at a restaurant. The bill comes in the amount of 47.28 dollars. The friends 
#..decide to split the bill evenly between them, after adding 15% tip for the service. Calculate the tip, the total amount to pay, 
#..and each friend's share, then output a message saying "Each person needs to pay: " followed by the resulting number.
bill = 47.28 # Assign "bill" variable with bill amount
tip = bill * 0.15 # Multiply by stated tip rate 
total = bill + tip # Sum the "total" of the "bill" and "tip"
share = total/2 # Divide "total" by number of friends dining
print("Each person needs to pay: " + str(share)) # Enter the required string and "share"

#2. Combine the variables to display the sentence "How do you like Python so far?" 
word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"
print(word1 + " " + word2 + " " + word3 + " " + word4 + " " + word5 + " " + word6 +  " " + word7)
#Alternatively:
print(word1, word2, word3, word4, word5, word6, word7)