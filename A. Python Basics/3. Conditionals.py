# ----
#---------------Comparing things-----------------
#Comparison operators return Booleab values (i.e., TRUE or FALSE)
print(10>1) #True
print("cat" == "dog") #False
print (1 != 2) #True
print(1 < "1") #Returns a type error (comparison of two different data types)
print(1 == "1") #False (different data types)

# Logical operators (AND, OR, NOT)
print("Yellow" > "Cyan" and "Brown" > "Magenta") #False (For "and" conjunctions, ALL component statements MUST be true to 
#..return a TRUE outcome. In this example, only the 1st component is true.)
#NB: The <, >, <=, and >= operators can be used with strings because the letters of the Alphabet have numeric codes in Unicode (aka 
#..ASCII values). The uppercase letters A to Z are represented by the Unicode values 65 to 90, while the lowercase letters a to z are 
#..represented by the Unicode values 97 to 122. 

print(25 > 50 or 1 != 2) #True (For "or" conjunctions, at least one component statements MUST be true to return a TRUE outcome.)
print(not 42 == "Answer") #True


#**********************************BRANCHING STATEMENTS (using IF and the like)****************************
#Branching is the ability of a program to alter its execution sequence
#The body of the IF block will only execute when the condition evaluates to true; otherwise it's skipped
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
hint_username("tunde") # No output. The function defines only a condition where username length is less than 3.
hint_username("Bo") #meets the function's condition. Prints the stated output

#if with else
def hint_username2(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        print("Valid username")
#The function is now more comprehensive, covering all possible scenarios
hint_username2("tunde") #Valid username
hint_username2("Bo") #Invalid username. Must be at least 3 characters long


#Another example:
def is_even(number):
    if number % 2 == 0:
        return True
    return False #the else statement can be entirely skipped, and replaced with its outcome instead
is_even(4) #True
is_even(17) #False


#-------else if/elif statements
def hint_username3(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        if len(username) > 15:
            print("Invalid username. Must be at most 15 characters long")
        else:
            print("Valid username")

#The code can be rewritten so that the else/if component is shrunk to "elif"
def hint_username3(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15: #else/if shrunk as elif
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Valid username")
hint_username3("Adeolatundesholaolaoluwasegunadeniyi") #Invalid username. Must be at most 15 characters long
hint_username3("Olasoji") #Valid username
hint_username3("Ho") #Invalid username. Must be at least 3 characters long

#----PRACTICE QUIZ
#If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of 
#..storage. A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this, can you fill in the gaps in the 
#..calculate_storage function below, which calculates the total number of bytes needed to store a file of a given size?
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = block_size/filesize
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = block_size % filesize
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size + partial_block_remainder
    return block_size
print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192