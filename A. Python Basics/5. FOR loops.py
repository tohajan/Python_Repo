#-------
# A FOR lopp iterates over a sequence of values.

for x in range(5):
    print(x) # Prints 0 -4 
# Notes about the range() function:
#   1. In Python and a lot of other programming languages, a range of numbers will start with the value 0 by default.
#   2. The list of numbers generated will be one less than the given value

friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)

values = [ 23, 52, 59, 37, 48 ]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1
print("Total sum: " + str(sum) + "; Average: " + str(sum/length))

#PS: when to use FOR vs WHILE loops:
#       FOR - when there's a sequence of elements that you want to iterate.
#       WHILE - when you want to repat an action until a codition changes.

product = 1
for n in range(1,10): #iterates over the range of numbers from 1 to 9
  product = product * n
print(product)


def to_celsius(x):
  return (x-32)*5/9
for x in range(0,101,10): # iterates over the numbers: 0, 10, 20 ... 100 (remember: 101 is not included in the range)
  print(x, to_celsius(x))



#**********************Nested FOR loops*************************************
for left in range(7):
  for right in range(left, 7):
    print("[" + str(left) + "|" + str(right) + "]", end=" ")
  print()

teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
  for away_team in teams:
    if home_team != away_team:
      print(home_team + " vs " + away_team)



#**********************Looping over a string*************************************