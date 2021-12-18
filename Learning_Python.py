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
#The amount of points for each exercise may change, because points don't exist yet
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