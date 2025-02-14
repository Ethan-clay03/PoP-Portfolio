# IN CLASS TEST 2 PART 2 [of 3]
# Note: you should NOT use input() or print() (other than for your own debugging purposes)
# Use the functions arguments as input and return values as output

# This section involves writing some more substantial functions focusing on grades from 2:2 -> 2:1 
# First class is possible by completing only part 1 and 2 but requires high accuracy
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# implement a function that takes a string as an argument and returns the number of vowels in the string.
# it should count both upper and lower case values
# you can assume input will always be a string
def count_vowels(s):
    string = s.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    
    for vowel in vowels:
        count += string.count(vowel)
    
    return count


# --------------------------------------------------------------------------------
# implement a function that takes a list of numbers and returns the largest value in that list
# you can assume input will always be a list of numbers
def largest_found(lst):
    highest_number = 0
    for number in lst:
        if number > highest_number:
            highest_number = number
            
    return highest_number

# --------------------------------------------------------------------------------
# implement a function that takes a 2D list of strings and a string to search for.
# The function should return a tuple of the string it found and the number of times it found it (number first then string). 
# If nothing is found it should still return the string that it searched for and indicate that it was found 0 times in the tuple.
# you can assume input will always be a list of strings but target may also be a number.
# If a number is provided for target you should search for the string representation of that number in the list of strings.
def find(lst, target):
    count = 0
    
    for current_list in lst:
        count += current_list.count(target)
    
    return (count, target)

# --------------------------------------------------------------------------------
# write a function that given a 2d array of strings (representing a tic tac toe board), checks to see if a player won
# The function should return 'x' or 'o' for a respective winner, 'tie' if there is no win possible 
# and '' (empty string) if there is no winner but play can still continue
# (the grid argument is a 2d list where 'x' and 'o' are used to represent player moves and available spaces are ' ')
# Bonus: for additional marks your function should also work where empty spaces in the grid are represented by numbers 1-9 not just an empty space
def check_win(grid):
    player = ''
    check_winner = check_player_win(grid)
    if (check_winner):
        player = check_winner
    if (check_draw(grid)):
        player = 'tie'
    return player


# Function to check if a player has won
def check_player_win(board):
    for i in range(0,3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
        
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    

# Function to check if the game is a draw
def check_draw(board):
    if " " not in board[0] and " " not in board[1] and " " not in board[2]:
        return True

def get_row(position_integer):
    return (position_integer - 1) // 3

def get_col(position_integer):
    return (position_integer - 1) % 3

def set_value_in_matrix(position_integer, player):
    row = get_row(position_integer)
    col = get_col(position_integer)
    
    value = get_tile_icon(player)
    
    board[row][col] = value