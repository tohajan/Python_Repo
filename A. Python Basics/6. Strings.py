# -----
name = "Sasha"
color = 'Gold'
# place = "Cambridge' #this line throws an error (only one type of quote [single or double] can be used in a single 
#..string, not a mixture of both
pet = "" #a string can also be empty

print("Name: " + name + ", Favorite color: " + color) #concatenation
"example" * 3 #prints exampleexampleexample
"example " * 3 #example example example 

pet = "loooooooooooooooooooooooooooooooog cat"
len(pet)


# ---------------------------Parts of a string ----------------------------------------------------------------------------
# ****Indexing
name = "Jaylen"
print(name[1]) #prints "a"
print(name[0]) #prints "J"
print(name[5]) #prints "n"
print(name[6]) #IndexError: string index out of range

text = "Random string with a lot of characters"
print(text[-1]) #prints "s" (last letter in the string)
print(text[-2]) #prints "r" (second to last letter in the string)


# *** Slicing
color = "Orange"
color[1:4] #prints "ran"

fruit = "Pineapple"
print(fruit[:4]) #prints "Pine" (up to, but not including, the index 4, i.e., the 5th letter)
print(fruit[4:]) #prints "pine" (from index 4, i.e., the 5th letter, to the end of the string)



# ---------------------------Creating new strings ----------------------------------------------------------------------------
message = "A kong string with a silly typo"
message[2] = "l" # TypeError: 'str' object does not support item assignment.
#This error is displayed because Python strings are immutable (non-modifiable). Instead, new strings can be created from
#..and existing one:
new_message = message[0:2] + "l" + message[3:]
print(new_message) #the target letter is now changed, in a new string

#A new string can be assigned to the same variable, in which case the new string ovewrites the old one
message = "This is a new message"
print(message)
message = "And another one" # this overwrited the initially assigned string ("This is a new message")
print(message) 

#To create new strings from an existing one, one needs to know the index position(s) of the target letter(s). This can be done
#..by requesting the index position using the "index method" (MORE ON METHODS IN A LATER LESSON):
"system".index("t") #prints "3" (index position of the letter t)
"Ijimere".index("r") #prints "5" (index position of the letter r)
"Adekunle".index("e") #prints "2" (when the letter occurs more than once, the first occurrence is prioritized)

pets="Cats & Dogs" #NB: spaces are also part of the string and thus have their own index position
pets.index("&") #prints "5"
pets.index("C") #prints "0"
pets.index("Dog") #prints "7" (index position of "D" which is the first letter in the substring)
pets.index("s") #prints "3" (index position of the first "s" in the string)
pets.index("x") #ValueError: substring not found ("x" is not in the string)

#Check if a substring/letter exists in a given string
"Dragons" in pets #prints "False"
"Cats" in pets #prints "True"

# A REAL LIFE PROBLEM
#The following function sifts through a collection of work emails, and replaces old domains with new domains
def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@" + old_domain)
    new_email = email[:index] + "@" + new_domain
    return new_email
  return email

replace_domain("toheeb@nmsu.edu", "nmsu.edu", "louisville.edu") #prints 'toheeb@louisville.edu'
replace_domain("toheeb@yahoo.co.uk", "yahoo.co.uk", "gmail.com") #prints 'toheeb@gmail.com'
replace_domain("tamust01@louisville.edu", "nmsu.edu", "louisville.edu") #prints 'tamust01@louisville.edu'


#-------------------------- More string methods ----------------------------------------------------------------------------
"Mountains".upper() #prints "MOUNTAINS"
"Mountains".lower() #prints "mountains"
#The following demonstrates a real-life application of the upper/lower method
answer = "YES"
if answer.lower() == "yes":
  print("User said yes") 

" yes ".strip() #prints "yes" (gets rid of surrounding spaces)
" yes ".lstrip() #prints "yes " (gets rid of whitespace to the left of the string)
" yes ".rstrip() #prints " yes" (gets rid of whitespace to the right of the string)

"The number of times e occurs in this string is 4".count("e") #counts the number of times a substring occurs in a string
#prints 4 (number of occurrences of the lette "e")

"Forest".endswith("rest") #checks if a string ends with a given substring
#returns True

#The isnumeric method checks whether a given string contains only numbers
"Forest".isnumeric() #False
"12345".isnumeric() #True
int("12345") + int("54321") #converts numeric strings to integers, which are then added together
#prints "66666"

#a collection of strings can be joined using the join method
" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]) #joins the strings with a space in-between each
#prints "This is a phrase joined by spaces"

"...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"])  #joins the strings with ellipses
# prints "This...is...a...phrase...joined...by...triple...dots"

"This is another example".split() #splits the sentence into single-word strings
#prints "['This', 'is', 'another', 'example']"