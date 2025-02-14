# IN CLASS TEST 1

# This set of questions we will assign variables 
# to answer multiple choice questions
# for example, answer by assigning the variable like this:
# answer_1 = 'a'
# --------------------------------------------------------------------------------

'''QUESTION 1
Which Python data type is used to represent a sequence of characters? 
a) Integer 
b) Float
c) String
d) Boolean
'''
answer_1 = 'c'
# --------------------------------------------------------------------------------

'''QUESTION 2
Which of the following creates the variable i and assigns it to 1? 
a) i = 1
b) x = 10
c) i == 1
d) i = 10
'''
answer_2 = 'a'
# --------------------------------------------------------------------------------

'''QUESTION 3
Which Python data type is used to represent a true or false value? 
a) Integer 
b) Float
c) String
d) Boolean
'''
answer_3 = 'd'

# --------------------------------------------------------------------------------
'''QUESTION 4
Which operator is used for assignment (assigning a variable)? 
a) >=
b) ==
c) !=
d) =
'''
answer_4 = 'd'
# --------------------------------------------------------------------------------
'''QUESTION 5
Which operator is used for comparison (comparing two values to see if they are equal)? 
a) = 
b) ==
c) !=
d) >=
'''
answer_5 = 'b'

# --------------------------------------------------------------------------------
'''QUESTION 6
Which of the following is not an expression? 
a) if(True):
b) len(lst)
c) x
d) 15 - 3
'''
answer_6 = 'a'

# --------------------------------------------------------------------------------
# This question requires you to return values from the following test functions
# replace 'pass' with 'return value' where value is the correct literal value

# return the value 256 from the function
def test_value_1():
    return 256

# return the value 3.1415 from the function
def test_value_2():
    return 3.1415

# return the boolean value false from the function
def test_value_3():
    return False

# return the string 'python' from the function
def test_value_4():
    return 'python'

# return a list containing integers counting from 1 - 5
def test_value_5():
    return [1,2,3,4,5]
# --------------------------------------------------------------------------------

# complete the following function such that it returns the result of adding arguments a and b
def add(a, b):
    c = a + b
    return c
    
# complete the following function such that it returns the result of subtracting arguments a and b
def subtract(a, b):
    c = a - b
    return c

# complete the following function such that it returns the result of multiplying arguments a and b
def multiply(a, b):
    c = a * b
    return c

# complete the following function such that it returns the result of dividing arguments a and b
# optionally, raise a runtime exception with the message 'bad div zero' if a divide by zero is attempted
def divide(a, b):
    try:
        c = a / b
    except ZeroDivisionError as error:
        return 'bad div zero'
    return c

# --------------------------------------------------------------------------------
# implement the fizz buzz function - integers are input into the argument n
# Return 'Fizz' if n is divisible by 3, 'Buzz' if n is divisible by 5,
# 'FizzBuzz' if n is divisible by both, and the string representation of n otherwise
# Dont forget to return not print!
def fizz_buzz(n):
    
    result = ""
    
    if (n % 3 == 0):
        result += "Fizz"
    
    if (n % 5 == 0):
        result += "Buzz"
    
    if (result == ''):
        result = str(n)
        
    return result


# --------------------------------------------------------------------------------
# take as input a string respresenting a choice in rock paper scissors from each player
# return the winner as a string in the format 'Player 1', or 'Player 2' or 'Tie'
# Optionally throw exceptions for nonsense string input and bad type input respectively
def rock_paper_scissors(player1, player2):
    
    try:
        player1 = sanitise_rps_string(player1)
        player2 = sanitise_rps_string(player2)
    except Exception as e:
        return e
    
    if (player1 == player2):
        return 'Tie'
    
    if ((player1 == 'rock') and (player2 == 'scissors')):
        result = 'Player 1'
    elif ((player1 == 'paper') and (player2 == 'rock')):
        result = 'Player 1'
    elif ((player1 == 'scissors') and (player2 == 'paper')):
        result = 'Player 1'
    else:
        result = 'Player 2'
    
    return result
    
#Sanitises input, checks if input is either rock paper or scissors. returns lower case string, otherwise throws an exception on invalid input
def sanitise_rps_string(input):
    if not(isinstance(input, str)):
        raise Exception("Sorry, please make sure your input is a string")
    
    input.lower()
    
    valid = False
    valid_inputs = ['rock', 'paper', 'scissors']
    for valid_item in valid_inputs:
        if (valid_item == input):
            valid = True
            break
    
    if (valid == False):
        raise Exception("Sorry, please make sure your input is either Rock, Paper or Scissors")
    
    return input
