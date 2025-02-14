from testlib import *
from math import pi
# Task 2

# -----------------------------------------------------------------

# Here is an example of how a complete task will look:                                         
value = 0
# Assign value to the result of the expression: 10 + 10
value = 10 + 10
testTaskExample(value)

# -----------------------------------------------------------------

#  ,--------.              ,--.         ,---.  
#  '--.  .--',--,--. ,---. |  |,-.     '.-.  |
#     |  |  ' ,-.  |(  .-' |     /      .-' .' 
#     |  |  \ '-'  |.-'  `)|  \  \     /   '-. 
#     `--'   `--`--'`----' `--'`--'    '-----' 
  
# -----------------------------------------------------------------
# Assign value to the integer expression:
# 100 / 2
value = 100 // 2
test_task2_1(value)

# -----------------------------------------------------------------

# Assign value to the result of the expression:
# 2.0 * 0.3 

value = 2.0 * 0.3
test_task2_2(value)
# -----------------------------------------------------------------
# assign value to the result of an expression that checks if 10 is greater than 5.  

value = 10 > 5
test_task2_3(value)
# -----------------------------------------------------------------


# assign value to the result of an expression that calculates the bitwise 'and' of 10 and 3.  
result = 10 & 3
test_task2_4(result)
# -----------------------------------------------------------------

# assign value to the result of comparing if variables 'a' and 'b' are equal:
a = 10.0 - 0.2 * 45.0
b = 1.0
#  Then pass value into the function:
result = (10.0 - 0.2 * 45.0) == (1.0)
test_task2_5(result)
# -----------------------------------------------------------------
                                    
# Create a variable with a value of 1.0 and add 0.5 
# Pass this new value to the test function.
a = 1.0
result = a + 0.5
test_task2_6(result)
# -----------------------------------------------------------------

# Create variables x and y where x is equal to 10 and y is equal to 5.
#  Divide x by y and the result to the function

x = 10
y = 5
result = x / y
test_task2_7(result)
# -----------------------------------------------------------------

# Create two variables one with a value true and one with false. 
# Pass the logical 'or' of these variables to the test fucntion.

a = True
b = False
result = a or b
test_task2_8(result)
# -----------------------------------------------------------------

# Create a single variable called x with a value 200
#  Double the variable using the '*=' operator and pass x to the test function.

result = 200
result *= 2
test_task2_9(result)
# -----------------------------------------------------------------

# Create a single variable called x with a value 1, use and operator to increment the variable by 1 and pass x 
# to the test function.

result = 1
result += 1
test_task2_10(result)
# -----------------------------------------------------------------


# Write the expression to calculate the area of a square with an edge that has a length of 20 units
# pass the variable storing that to the function:
result = 20 * 20
test_task2_11(result)
# -----------------------------------------------------------------
                            
# Calculate the area of a circle with a radius of 2 units with appropriate precission.
result = pi * (2 ** 2)
test_task2_12(result)
# -----------------------------------------------------------------

# Calculate the average (mean) of the values a = 3, b = 7, c = 4
result = (3 + 7 + 4) / 3
test_task2_13(result)
# -----------------------------------------------------------------

# Using the Einsteins famous E=MC^2 calculate E where M is 2
# note: C is usually expressed in m/s
result = 2*299792458**2
test_task2_14(result)
# -----------------------------------------------------------------

# Given x as 256 set y to 64 using x and a bitwise shift (not just writing the number!)
x = 256
y = x >> 2
test_task2_15(y)
# -----------------------------------------------------------------

print ("All tests passed")