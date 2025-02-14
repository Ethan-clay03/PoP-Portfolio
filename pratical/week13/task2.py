# Welcome to Task 2
# here you can write solutions to some problems that you can come up with yourself.
# then in test-tesk2.py, call the functions and test the results.

# a good starting point for this is to explore string manipulation problems.

def example(beep):
    if(beep == 'beep'):
        return 'boop'
    else:
        return 'nope'
    

def fizz_buzz(n):
    
    result = ""
    
    if (n % 3 == 0):
        result += "Fizz"
    
    if (n % 5 == 0):
        result += "Buzz"
    
    if (result == ''):
        result = str(n)
        
    return result