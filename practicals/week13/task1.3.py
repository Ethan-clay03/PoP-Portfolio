# Note there are no tests for task 1
# Explore the basic concepts and get a feel for the difference between
#  writing (defining) functions and calling them
# Run this file to explore the programming concepts
# Be sure to play around and change things to see what works and what doesn't!
# ------------------------------------------------------------------------------

# Tutorial: Writing and Calling Functions that return values

# We can also get values out of a function by returning a value
# remember expressions are evaluated to a value before returning
def double_it(x):
    # using the return keyword we can evaluate x times 2 and return the value from that:
    return x * 2

# We can also specify a type for these functions 
# if we want to ensure only a certain type is passed in:
def add_five(y: int) -> int:
    y += 5
    return y + 5

# given our example functions above we can call them
# notice that as these functions do not print we must capture/use the values 
# they return (for example in a variable)
result1 = double_it(3)
print(f"Calling double_it with argument 3 gets us: {result1}")  # we can print the value after we capture it

# try passing something that isn't a number to this function!
result2 = add_five(4)
print(f"calling add_five and passing it 4: {result2}")

# It's actually really important that we define functions to return things
# rather than just printing inside the function for example
# This is because it allows us to chain together useful functions:

result3 = double_it(add_five(2))  # Double the result of adding 5 to 2
print(f"Double of (2 + 5): {result3}")

# This allows us to build up or 'compose' functions, a very powerful way of programming.
print( 'your number is : ' + str(input('give me a number: ')))