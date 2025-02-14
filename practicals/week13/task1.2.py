# Note there are no tests for task 1
# Explore the basic concepts and get a feel for the difference between
#  writing (defining) functions and calling them
# Run this file to explore the programming concepts
# Be sure to play around and change things to see what works and what doesn't!
# ------------------------------------------------------------------------------

# Tutorial: Writing and Calling Functions with Arguments

# We can pass data from outside a function into a function.
# We do this by providing names (very much like variables) inside the round brackets
# These then represent placeholders for values that are passed into the function when called
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# we can run the greet function by passing it values and it will then make use of those values
# call the greet function a few more times with different values passed in...
greet("John", 30)  

# ------------------------------------------------------------------------------
# we can also add default arguments to a function.
# lets add favorite_food and make it default to pizza (that's a good bet!)
def introduce(name, age, favorite_food="Pizza"):
    print(f"Hi, my name is {name}, I'm {age} years old, and I love {favorite_food}!")

# Call the introduce function and experiment with different values like below:

# introduce("Jane", 25)  
# introduce("Nate", 21, 'curry')  
# introduce("Ben", favorite_food="Tacos", age = 20)

# Notice that when calling functions, the order must match or 
# the argument names can be used to set arguments in a different order!

# ------------------------------------------------------------------------------

# Task: Write a function that takes a number and prints out hello world that many times.
# Don't forget to define it AND to call it (so that it actually runs)


def hello(limit):
    for x in range (0,limit):
        print ("Hello world")
        
# hello(3)