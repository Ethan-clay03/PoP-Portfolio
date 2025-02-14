# Note there are no tests for task 1
# Explore the basic concepts and get a feel for conditionals, loops and exceptions
# Run this file to explore the programming concepts
# Be sure to play around and change things to see what works and what doesn't!

# Exceptions are a form of control flow used for errror handling
# It's important to explore how they are used and what it means for managing errors

# Example 1: Basic try-except block
try:
    x = 5 / 0  # intentional division by zero
except ZeroDivisionError:
    print("Error: Division by zero!")

# Example 2: Handling multiple exceptions
try:
    even_numbers = [2, 4, 6, 8]
    print(even_numbers[5])  # intentional index out of range
except ZeroDivisionError:
    print("Denominator cannot be 0.")
except IndexError:
    print("Index out of bound.")

# Example 3: Using finally block
try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print(result)
except:
    print("Error: Denominator cannot be 0.")
finally:
    print("This is the finally block.")

# Example 4: Raising custom exceptions
class InvalidInputError(Exception):
    pass

try:
    error = False
    user_input = int(input("Enter a number: "))
    if user_input < 0:
        raise InvalidInputError("Invalid input: must be non-negative")
except (InvalidInputError, ValueError) as e:
    error = True
    print(f"Error: {e}")
finally:
    if error == False:
        print (f"Valid number of {user_input} was entered")

