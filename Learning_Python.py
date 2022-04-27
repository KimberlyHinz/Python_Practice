# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 22:57:26 2021

@author: Kim Hinz
"""

# This program includes my learning progress of Python!

# %% Python Syntax
# To print a message:
print("Hello! My name is Kim.")

# Assigning variables
todays_date = "2021/11/30"
number = 5

# Math
##  Combinations of arithmetical operators follow the usual order of operations.
mirthful_addition = 12381 + 91817
amazing_subtraction = 981 - 312
trippy_multiplication = 38 * 902
happy_division = 540 / 45
sassy_combinations = 129 * 1345 + 120 / 6 - 12

is_this_number_odd = 15 % 2
is_this_number_divisible_by_seven = 133 % 7

powers = 4**2

# Updating variables (and more math)
money_in_wallet = 40
sandwich_price = 7.50
sales_tax = .08 * sandwich_price
 
sandwich_price += sales_tax                                                # IMPORTANT WHEN CHANGING THE VALUE
money_in_wallet -= sandwich_price

# Python DOES NOT care about the numeric data type!
7/2 
7.3/6

# Multi-line strings using triple quotes
address_string = """136 Whowho Rd
Apt 7
Whosville, WZ 44494"""

# Can also use triple quotes for multi-line comments
"""The following piece of code does the following steps:
takes in some input
does An Important Calculation
returns the modified input and a string that says "Success!" or "Failure..."
"""

# Boolean
a = True
b = False

# Converting between datatypes
age = 13
print("I am " + str(age) + " years old!")

number1 = "100"
number2 = "10"
 
string_addition = number1 + number2 
#string_addition now has a value of "10010"
 
int_addition = int(number1) + int(number2)
#int_addition has a value of 110

string_num = "7.5"
print(int(string_num))                                                     # THIS DOES NOT WORK IN PYTHON 3
print(float(string_num))

# REVIEW
skill_completed = "Python Syntax"

exercises_completed = 13
#The amount of points for each exercise may change, because points don"t exist yet
points_per_exercise = 5

point_total = 100
point_total += exercises_completed * points_per_exercise

print("I got " + str(point_total) + " points!")

# %% Strings and Console Output
# Escaping characters in strings
test = 'There\'s a snake in my boot!'
print(test)
test2 = "There's a snake in my boot!"                                      # Escaping is only needed when using the same type
print(test2)                                                               # Because this works

# Indices in strings
c = "cats"[0]
n = "Ryan"[3]

# String methods
## Length of strings
parrot = "Norwegian Blue"
print(len(parrot))

## Make it all lowercase
print(parrot.lower())                                                      # Methods that use dot notation only work with strings

## Make it all UPPERCASE
print(parrot.upper())

## Turn non-strings into strings
pi = 3.14
print(str(pi))                                                             # len() and str() can work on other data types.

# String formatting with %
string_1 = "Camelot"
string_2 = "place"

print("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))

day = 6
print("03 - %s - 2019" %  (day))
# 03 - 6 - 2019
print("03 - %02d - 2019" % (day))
# 03 - 06 - 2019
"""If you’d like to print a variable that is an integer, you can “pad” it with zeros using %02d. 
The 0 means “pad with zeros”, the 2 means to pad to 2 characters wide, and the d means the number 
is a signed integer (can be positive or negative)."""

name = "Alex"
quest = "Teaching Python"
color = "Blue"
# Backslash allows multi-line function, best now use it though since it all doesn't run at once with Ctrl+Enter
print("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))                   # Num of %s terms == num of var in parentheses
    
# %% Date and Time
# Import libraries
from datetime import datetime

# Current date and time
now = datetime.now()
print(now)

# Specifics
print(now.year)
print(now.month)
print(now.day)
print(now.hour)

# Print in specific format
print("%02d/%02d/%04d" % (now.month, now.day, now.year))
print("%02d:%02d:%02d" % (now.hour, now.minute, now.second))
print("%02d/%02d/%04d %02d:%02d:%02d" % (now.month, now.day, now.year, now.hour, now.minute, now.second))

# %% Conditionals and Control Flow
# Comparators
# Equal to (==)
# Not equal to (!=)
# Less than (<)
# Less than or equal to (<=)
# Greater than (>)
# Greater than or equal to (>=)
bool_one = 3 < 5
## HERE!!
# Boolean operators
# and, which checks if both the statements are True;
bool_one = 1 < 2 and 2 < 3
bool_two = 1 < 2 and 2 > 3
# or, which checks if at least one of the statements is True;
bool_one = 1 < 2 or 2 > 3
bool_two = 1 > 2 or 2 > 3
# not, which gives the opposite of the statement.
not 3 ** 4 < 4 ** 3
not not False

# There is an order to boolean operators: not --> and --> or (unless there are parentheses)
False or not True and True
False and not True or True
True and not (False or False)
not not True or False and not True
False or not (True and True)
## HERE
# Conditional statement syntax
if 8 < 9:
  print("Eight is less than nine!")

def using_control_once():
    if 5 > 1:
        return "Success #1"
print(using_control_once())

if 8 > 9:
  print("I don't get printed!")
else:
  print("I get printed!")
  
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print(greater_less_equal_5(4))
print(greater_less_equal_5(5))
print(greater_less_equal_5(6))

# REVIEW
def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80 and grade <= 89:
        return "B"
    elif grade >= 70 and grade <= 79:
        return "C"
    elif grade >= 65 and grade <= 69:
        return "D"
    else:
        return "F"
      
# This should print an "A"      
print(grade_converter(92))

# This should print a "C"
print(grade_converter(70))

# This should print an "F"
print(grade_converter(61))

# %% PygLatin
pyg = 'ay'

print("Welcome to the Pig Latin Translator!")

original = input("Enter a word: ")                                         # input() used to be raw_input()

if len(original) > 0 and original.isalpha():
  print(original)
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
else:
  print("empty")

# %% Functions
def spam():
  """ Prints 'Eggs!' to the console."""
  print("Eggs!")

spam()

def square(n):
  """Returns the square of a number."""
  squared = n ** 2
  print("%d squared is %d." % (n, squared))
  return squared
  
square(10)

def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print("%d to the power of %d is %d." % (base, exponent, result))

power(37, 4)  # Add your arguments here!

def one_good_turn(n):
  return n + 1
    
def deserves_another(n):
  return one_good_turn(n) + 2

def cube(number):
  return number * number * number

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False

import math                                                                # Imports the whole library/module, but have call it
print(math.sqrt(25))    

from math import sqrt                                                      # Imports only the sqrt function
sqrt(25)

# from math import *                                                         # Imports whole module, and don't need math.
sqrt(25)

# See all functions in a module
import math # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print(everything) # Prints 'em all!

# Built-in functions
maximum = max(2, 5, 10000)
print(maximum)

minimum = min(3, 8, 1001)
print(minimum)

absolute = abs(-42)
print(absolute)

print(type(3))
print(type(5.6))
print(type("Hello"))

def distance_from_zero(x):
  if type(x) in (int, float):
    return abs(x)
  else:
    return "Nope"

# %% Taking a Vacation
def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  total = 40 * days
  if days >= 3 and days < 7:
    total -= 20
  elif days >= 7:
    total -= 50
  return total

def trip_cost(city, days, spending_money):
  return hotel_cost(days - 1) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

print(trip_cost("Los Angeles", 5, 600))

# %% Python Lists and Dictionaries
list_name = ["item_1", "item_2"]
empty_list = []                                                                # Lists can also be empty

zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]

if len(zoo_animals) > 3:
  print("The first animal at the zoo is the " + zoo_animals[0])                # Indexing starts at 0
  print("The second animal at the zoo is the " + zoo_animals[1])
  print("The third animal at the zoo is the " + zoo_animals[2])
  print("The fourth animal at the zoo is the " + zoo_animals[3])

zoo_animals[2] = "hyena"                                                       # Can easily change the items

suitcase = [] 
suitcase.append("sunglasses")
list_length = len(suitcase)
print("There are %d items in the suitcase." % (list_length))
print(suitcase)

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
first = suitcase[0:2]                                                          # NOTE: THESE EACH TAKE ONLY TWO ITEMS. I KNOW, IT'S STUPID!
middle = suitcase[2:4]                                                         # First index is item_you_want - 1
last =  suitcase[4:6]                                                          # Second index last item you want

# THIS ALSO WORKS FOR LISTS!!!
animals = "catdogfrog"
cat = animals[:3]
dog = animals[3:6]
frog = animals[6:]

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")                                             # Find the index of an item
animals.insert(2, "cobra")                                                     # Inserts an item at that index
print(animals)

### FOR LOOPS
my_list = [1,9,3,8,5,7]
for number in my_list:
  print(number * 2)

### Sort Lists
start_list = [5, 3, 1, 2, 4]
square_list = []
for number in start_list:
  square_list.append(number ** 2)
square_list.sort()
print(square_list)

### Creating dictionaries
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print(residents["Puffin"]) # Prints Puffin's room number
print(residents["Sloth"])
print(residents["Burmese Python"])

menu = {} # Empty dictionary
menu["Chicken Alfredo"] = 14.50 # Adding new key-value pair
menu["Spaghetti"] = 13.50
menu["Lasagne"] = 14.50
menu["Bolognese"] = 15.50

print("There are " + str(len(menu)) + " items on the menu.")

zoo_animals = {"Unicorn" : "Cotton Candy House", 
               "Sloth" : "Rainforest Exhibit",
               "Bengal Tiger" : "Jungle House",
               "Atlantic Puffin" : "Arctic Exhibit",
               "Rockhopper Penguin" : "Arctic Exhibit"}
del zoo_animals["Unicorn"]
del zoo_animals["Sloth"] # Can"t put these three together in one commmand :(
del zoo_animals["Bengal Tiger"]

zoo_animals["Rockhopper Penguin"] = "Vet"

print(zoo_animals)

### Back to lists
backpack = ["xylophone", "dagger", "tent", "bread loaf"]
backpack.remove("dagger")

### SUMMARY
inventory = {
  "gold" : 500,
  "pouch" : ["flint", "twine", "gemstone"], # Assigned a new list to "pouch" key
  "backpack" : ["xylophone","dagger", "bedroll","bread loaf"]
}

# Adding a key "burlap bag" and assigning a list to it
inventory["burlap bag"] = ["apple", "small ruby", "three-toed sloth"]

# Sorting the list found under the key "pouch"
inventory["pouch"].sort() 

# Your code here
inventory["pocket"] = ["seashell", "strange berry", "lint"]

inventory["backpack"].sort()

inventory["backpack"].remove("dagger")

inventory["gold"] += 50

# %% A Day at the Supermarket
names = ["Adam", "Alex", "Mariah", "Martine", "Columbus"]

for x in names:
  print(x)

# Loop through the webster dictionary and print all of the definitions.
webster = {"Aardvark" : "A star of a popular children's cartoon show.",
           "Baa" : "The sound a goat makes.",
           "Carpet": "Goes on the floor.",
           "Dab": "A small amount."}

for definitions in webster:
  print(webster[definitions])

# Expand the for loop to do more
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for number in a:
  if number % 2 == 0:
    print(number)

# Functions can also take lists as inputs and do something with them
def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count = count + 1
  return count

# Loop through strings
for letter in "Codecademy":
  print(letter)
    
print # Empty lines to make the output pretty
print

word = "Programming is fun!"

for letter in word:
  # Only print out the letter i
  if letter == "i":
    print(letter)
    
# Core project
prices = {"banana" : 4, "apple" : 2, "orange" : 1.5, "pear" : 3}
stock = {"banana" : 6, "apple" : 0, "orange" : 32, "pear" : 15}

for key in prices:
  print(key)
  print("price: %s" % prices[key])
  print("stock: %s" % stock[key])
  
total = 0
for key in prices:
  value = prices[key] * stock[key]
  print(value)
  total = total + value
print(total)

# Now from the shopper POV. Make a consumer interface!
shopping_list = ["banana", "orange", "apple"]

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
    
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total += prices[item]
      stock[item] -= 1
  return total

print(compute_bill(shopping_list))

# %% Student Becomes the Teacher
lloyd = {"name": "Lloyd",
         "homework": [90.0, 97.0, 75.0, 92.0],
         "quizzes": [88.0, 40.0, 94.0],
         "tests": [75.0, 90.0]}

alice = {"name": "Alice",
         "homework": [100.0, 92.0, 98.0, 100.0],
         "quizzes": [82.0, 83.0, 91.0],
         "tests": [89.0, 97.0]}

tyler = {"name": "Tyler",
         "homework": [0.0, 87.0, 75.0, 22.0],
         "quizzes": [0.0, 75.0, 78.0],
         "tests": [100.0, 100.0]}

students = [lloyd, alice, tyler]

for student in students:
  print(student["name"])
  print(student["homework"])
  print(student["quizzes"])
  print(student["tests"])

def average(numbers):
  total = sum(numbers)
  total = float(total)
  total = total / len(numbers)
  return total

print(average(lloyd["homework"]))

def get_average(student):
  homework = (average(student["homework"])) # 10%
  quizzes = (average(student["quizzes"]))   # 30%
  tests = (average(student["tests"]))       # 60%
  return (homework * 0.10) + (quizzes * 0.30) + (tests * 0.60)

def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >= 80 and score < 90:
    return "B"
  elif score >= 70 and score < 80:
    return "C"
  elif score >= 60 and score < 70:
    return "D"
  else:
    return "F"

print(get_letter_grade(get_average(lloyd)))

def get_class_average(class_list):
  results = []
  for student in class_list:
    results.append(get_average(student))
  return average(results)

print(get_class_average(students))
print(get_letter_grade(get_class_average(students)))

# %% Lists and Functions
n = [1, 3, 5]
print(n[1]) # Prints the second item in a list

n[1] = n[1] * 5 # Modify second item
print(n)

n.append(4) # Add an item
print(n)

# Three ways to remove an item from a list:
n = [1, 3, 5]
n.pop(1) # Returns 3 (the item at index 1)
print(n)

n.remove(1) # Removes 1 from the list, NOT the item at index 1
print(n)

del(n[1]) # Doesn't return anything
print(n)


# Now onto functions
number = 5
def my_function(x):
  return x * 3
print(my_function(number))

m = 5
n = 13
def add_function(x, y):
  return x + y
print(add_function(m, n))

n = "Hello"
def string_function(s):
  return s + "world"
print(string_function(n))

def list_function(x):
  return x[1]
n = [3, 5, 7]
print(list_function(n))

n = [3, 5, 7]
def list_extender(lst):
  lst.append(9)
  return lst
print(list_extender(n))

n = [3, 5, 7]
def print_list(x):
  for i in range(0, len(x)):
    print(x[i])
print(print_list(n))

n = [3, 5, 7]
def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
  return x
print(double_list(n))

# Range
range(6)        # => [0, 1, 2, 3, 4, 5]
range(1, 6)     # => [1, 2, 3, 4, 5]
range(1, 6, 3)  # => [1, 4]

# Iterating over a list in a function:
# Method 1
n = [3, 5, 7]
def total(numbers):
  result = 0
  for item in numbers:
    result += item
  return result
# Method 2
n = [3, 5, 7]
def total(numbers):
  result = 0
  for n in range(len(numbers)):
    result += numbers[n]
  return result

# Using strings in lists in functions
n = ["Michael", "Lieberman"]
def join_strings(words):
  result = ""
  for wrd in words:
    result = result + wrd
  return result
print(join_strings(n))

# Using two lists as two arguments in a function
m = [1, 2, 3]
n = [4, 5, 6]
def join_lists(x, y):
  return x + y
print(join_lists(m, n))

# Using a list of lists in a function
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
def flatten(lists):
  results = []
  for numbers in lists:
    for item in numbers:
      results.append(item)
  return results
print(flatten(n))

# %% Battleship
from random import randint

board = []
for n in range(5):
  board.append(["O"] * 5)

def print_board(board_in):
  for row in range(len(board)):
    print(" ".join(board[row]))
    
print_board(board)

def random_row(board_in):
  return randint(0, len(board_in) - 1)

def random_col(board_in):
  return randint(0, len(board_in) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    print("Turn: ", turn + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")  
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            print_board(board)
        if turn == 3:
            print("Game Over")
            
# Make it more complex!

# Make multiple battleships: you’ll need to be careful because you need to 
# make sure that you don’t place battleships on top of each other on the 
# game board. You’ll also want to make sure that you balance the size of 
# the board with the number of ships so the game is still challenging and 
# fun to play.

# Make battleships of different sizes: this is trickier than it sounds. All 
# the parts of the battleship need to be vertically or horizontally 
# touching and you’ll need to make sure you don’t accidentally place part 
# of a ship off the side of the board.

# Make your game a two-player game.

# Use functions to allow your game to have more features like rematches, 
# statistics and more!

# %% Loops
count = 0
if count <= 9: # Will only run once, but will change count
  print("Hello, I am an if statement and count is", count)
  count += 1
while count <= 9: # Will continue to run until count is 10
  print("Hello, I am a while and count is", count)
  count += 1
  
loop_condition = True
while loop_condition: # The argument can be as simple as this
  print("I am a loop")
  loop_condition = False
  
num = 1
while num <= 10:
  print(num ** 2)
  num += 1
  
choice = input("Enjoying the course? (y/n)")
while choice != "y" and choice != "n":
  choice = input("Sorry, I didn't catch that. Enter again: ")

count = 0
while True:
  print(count)
  count += 1
  if count >= 10:
    break # This is another way to exit a while loop
    
# While AND Else:
# The Else will execute if the loop is never entered or if the loop exits normally.
# If the loop exits as the result of a break, the else will not be executed.
import random
print("Lucky Numbers! 3 numbers will be generated.")
print("If one of them is a '5', you lose!")
count = 0
while count < 3:
  num = random.randint(1, 6)
  print(num)
  if num == 5:
    print("Sorry, you lose!")
    break
  count += 1
else:
  print("You win!")

# from random import randint
# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
  guess = int(input("Your guess: "))
  if guess == random_number:
    print("You win!")
    break
  guesses_left -= 1
else:
  print("You lose.")
  
# FOR LOOPS
print("Counting...")
for i in range(21):
  print(i)

hobbies = []
for i in range(3):
  hobby = input("Add a hobby: ")
  hobbies.append(hobby)
print(hobbies)

word = "eggs!"
for char in word:
  print(char)   # Will print each individual character in a string
  
phrase = "A bird in the hand..."
for char in phrase:
  if char == "A" or char == "a":
    print("X", end = "") # This "end" prevents a newline from being added
  else:
    print(char, end = "")

numbers  = [7, 9, 12, 54, 99] # Loop through a list
print("This list contains: ")
for num in numbers:
  print(num)

# Looping through a dictionary
# You get the key which you can use to get the value
d = {"a": "apple", "b": "berry", "c": "cherry"}
for key in d:
  print(key + " " + d[key])

choices = ["pizza", "pasta", "salad", "nachos"]
print("Your choices are:")
for index, item in enumerate(choices): # enumerate() numbers the items in a list and puts them into index
  print(index + 1, item) # index + 1 makes it start at 1, rather than 0. You can also put enumerate(choices, 1) for the same effect
  
# It’s also common to need to iterate over two lists at once.
# zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list
# zip can handle three or more lists as well!
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
for a, b in zip(list_a, list_b):
    if a > b:
      print(a)
    elif b > a:
      print(b)

# Just like with while, for loops may have an else associated with them.
# The else statement is executed after the for, but only if the for ends normally—that is, not with a break. 
fruits = ["banana", "apple", "orange", "strawberry", "pear", "grape"]

print("You have...")
for f in fruits:
  if f == "tomato":
    print("A tomato is not a fruit!") # (It actually is.)
    break
  print("A", f)
else:
  print("A fine selection of fruits!")

# %% Practice Makes Perfect
def is_even(x):
  if x % 2 == 0:
    return True
  else:
    return False

def is_int(x):
  if x == int(x):
    return True
  else:
    return False

def digit_sum(x):
  as_string = str(x)
  total = 0
  for char in as_string:
    total += int(char)
  return total

def factorial(x):
  total = 1
  while x >= 1:
    total = total * x
    x -= 1
  return total

def is_prime(x):
  if x < 2:
      return False
  else:
      for n in range(2, x - 1):
          if x % n == 0:
              return False
      return True    

def reverse(text):
  rev = ""
  for char in text:
    rev = char + rev
  return rev

def anti_vowel(text):
  vowelless = ""
  for char in text:
    if char in ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u"):
      vowelless = vowelless
    else:
      vowelless = vowelless + char
  return vowelless
print(anti_vowel("Hey"))

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
  total = 0
  for char in word:
    char = char.lower()
    total += score[char]
  return total

def censor(text, word):
  split_text = text.split(" ")
  new_list = []
  for item in split_text:
      if item == word:
          new = "*" * len(word)
          new_list.append(new)
      else:
          new_list.append(item)
  new_text = " ".join(new_list)
  return new_text

def count(sequence, item):
  cnt = 0  
  for n in sequence:
      if n == item:
          cnt += 1
  return cnt

def purify(sequence):
  even_sequence = []
  for num in sequence:
    if num % 2 == 0:
      even_sequence.append(num)
  return even_sequence

def product(sequence):
  total = 1
  for num in sequence:
    total = total * num
  return total

def remove_duplicates(old_list):
  new_list = []
  for item in old_list:
      if item not in new_list:
          new_list.append(item)
  return new_list

def median(numbers):
  sort_nums = sorted(numbers)
  len_nums = len(sort_nums)
  if len_nums % 2 == 1:
      mid_num = int(len_nums / 2) + 1
      return sort_nums[mid_num - 1]
  else:
      mid_num1 = int(len_nums / 2)
      mid_num2 = int(len_nums / 2) + 1
      return float(sort_nums[mid_num1 - 1] + sort_nums[mid_num2 - 1]) / 2

# %% Exam Statistics
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
print("Grades:", grades)

def print_grades(grades_input):
  for val in range(len(grades_input)):
    print(grades_input[val])

print_grades(grades)

def grades_sum(scores):
  summed = 0
  for score in scores:
    summed += score
  return summed

print(grades_sum(grades))

def grades_average(grades_input):
  summed = grades_sum(grades_input)
  avrg = summed / float(len(grades_input))
  return avrg

print(grades_average(grades))

def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    variance += (average - score) **2
  variance /= float(len(scores))
  return variance

print(grades_variance(grades))

def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)
print(grades_std_deviation(variance))

# %% Advanced Topics in Python
my_dict = {"First_Name": "Danielle", "Last_Name": "Smith", "Age": 32}
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
# .items() returns an array of tuples
# .keys() returns a list of the keys
# .values() returns a list of the values

for key in my_dict:
  print(key, my_dict[key])

evens_to_50 = [i for i in range(51) if i % 2 == 0]
print(evens_to_50)

even_squares = [x ** 2 for x in range(1, 11) if (x **2) % 2 == 0]
print(even_squares)

cubes_by_four = [x ** 3 for x in range(1, 11) if (x ** 3) % 4 == 0]
print(cubes_by_four)

# Where start describes where the slice starts (inclusive), 
# end is where it ends (exclusive), and 
# stride describes the space between items in the sliced list. 
# For example, a stride of 2 would select every other item from 
# the original list to place in the sliced list.
l = [i ** 2 for i in range(1, 11)] # Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(l[2:9:2])

to_five = ['A', 'B', 'C', 'D', 'E']
print(to_five[3:]) # prints ['D', 'E'] 
print(to_five[:2]) # prints ['A', 'B']
print(to_five[::2]) # print ['A', 'C', 'E']

my_list = range(1, 11) # List of numbers 1 - 10
print(my_list[::2]) # Prints the odd numbers
backwards = my_list[::-1] # Saves my_list backwards!

to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::10][::-1]
print(backwards_by_tens)

# Anonymous functions
my_list = range(16)
print(filter(lambda x: x % 3 == 0, my_list))

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print(filter(lambda x: x == "Python", languages))

squares = [x ** 2 for x in range(1, 11)]
print(filter(lambda x: x >= 30 and x <= 70, squares))

movies = {"Monty Python and the Holy Grail": "Great", 
          "Monty Python's Life of Brian": "Good",
          "Monty Python's Meaning of Life": "Okay"}
print(movies.items())

threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-1][::2]

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != "X", garbled)
print(message)

# %% Introduction to Bitwise Operators
# 1010 == 10
# 8's bit  4's bit  2's bit  1's bit
#       1        0        1        0 
#       8   +    0    +   2    +   0  = 10 

print(0b1),    #1
print(0b10),   #2
print(0b11),   #3
print(0b100),  #4
print(0b101),  #5
print(0b110),  #6
print(0b111)   #7
print("******")
print(0b1 + 0b11)
print(0b11 * 0b11)

print(bin(1))
print(bin(2))
print(bin(3))
print(bin(4))
print(bin(5))

print(int("111",2))
print(int("0b100",2))
print(int(bin(5),2))
print(int("0b11001001", 2))

# %% Introduction to Classes



# %% Classes



# %% File Input/Output
