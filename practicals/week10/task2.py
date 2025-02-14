# the age old interview question
# Return 'Fizz' if n is divisible by 3, 'Buzz' if n is divisible by 5,
# 'FizzBuzz' if n is divisible by both, and the string representation of n otherwise
# Dont forget to return not print!
def fizz_buzz(n):
    n += 1 # Range does not inclue the value entered
    for x in range (1, n):
        output = "";
        
        if (x % 3 == 0):
            output += "Fizz"
        
        if (x % 5 == 0):
            output += "Buzz"
        
        if (output == ""):
            output = x;

        print (f"{x} Number is: {output}\n")

# take a list of numbers in and sort them smallest to largest
# return the sorted list
def sort_list(list):
    list.sort()
    return list

# implement a binary search to see if a list contains a given number
# Note: You should first sort the list (using your sort_list function!)
# Return -1 in cases where the target is not found
def binary_search(list, low, high, target):
    if high >= low:
 
        mid = (high + low) // 2
 
        if list[mid] == target:
            return 1
 
        elif list[mid] > target:
            return binary_search(list, low, mid - 1, target)
  
        else:
            return binary_search(list, mid + 1, high, target)
 
    else:
        return -1

def play_rock_paper_scissors():
    player_1 = rps_input(1)
    player_2 = rps_input(2)
    
    fight_to_the_death(player_1, player_2)

def fight_to_the_death(player_1, player_2):
    
    if (player_1 == player_2):
        print(f("Oh no it is a tie, you both chose {player_1}"))
    
    if player_1 == 'rock':
        if player_2 == 'scissors':
            print("Player 1 won with rock, smashing player 2's scissors!")
        elif player_2 == 'paper':
            print("Player 2 won with paper, covering player 1's rock!")
    elif player_1 == 'scissors':
        if player_2 == 'rock':
            print("Player 2 won with rock, smashing player 1's scissors!")
        elif player_2 == 'paper':
            print("Player 1 won with scissors, cutting up player 2's paper!")
    elif player_1 == 'paper':
        if player_2 == 'scissors':
            print("Player 2 won with scissors, cutting up player 1's paper!")
        elif player_2 == 'rock':
            print("Player 1 won with paper, covering player 2's rock!")
    else:
        print("Something went wrong... returning to battle stations")
        return play_rock_paper_scissors()
    
    
    
    
def rps_input(player):
    user_input = input(f"Player {player}, rock, paper or scissors: ").strip().lower()
    valid_inputs = ['rock', 'paper', 'scissors']
    result = user_input in valid_inputs
    if (result == False):
        print (f"Please enter a valid selection Player {player}")
    
    return user_input
    
    
#write the core function to game of life - given a cells current state
# return the correct output state
def game_of_life(state):
    pass

#Fizz buzz game
fizz_buzz(0); #Takes an argument for the amount of numbers you want to generate for the fizz buzz game


#Binary search
sorted_list = sort_list([1,2,3,4,4,3,2,1,1,1,1]);
find = 4
result = binary_search(sorted_list, 0, len(sorted_list)-1, find)
# print (result)

play_rock_paper_scissors()
