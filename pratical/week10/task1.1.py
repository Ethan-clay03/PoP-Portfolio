# Note there are no tests for task 1
# Explore the basic concepts and get a feel for conditionals, loops and exceptions
# Run this file to explore the programming concepts
# Be sure to play around and change things to see what works and what doesn't!

"""
Interactive If Statement Example
--------------------------------

In this example, we'll explore the basics of if statements in Python.
Comments will provide explanations and hints throughout the code.
"""

# If x is greater than y, print "x is bigger"
x = 5
y = 3
if x > y:
    print("x is bigger")  # Comment: This block will execute if the condition is true

# If Statement with Else Clause
# If z is greater than w, print "z is bigger", otherwise print "z is smaller"
z = 2
w = 4
if z > w:
    print("z is bigger")
else:
    print("z is smaller")  # Comment: This block will execute if the condition is false

# If Statement with Multiple Conditions
# If the person is a student (True) and age is 20 or less, print "You're a young student"
age = 25
is_student = True
if is_student and age <= 20:
    print("You're a young student")  # Comment: Both conditions must be true for this block to execute

# If Statement with Not Operator
# If the person does NOT have a car (False), print "You don't own a car"
has_car = False
if not has_car:
    print("You don't own a car")  # Comment: This block will execute if the condition is false

# Interactive Example
# If the user input is greater than 10, print "You entered a large number"
user_input = int(input("Enter a number: "))
if user_input > 10:
    print("You entered a large number")  # Comment: Ask the user to try again if they enter a small number

# Your turn:
# uncomment the code between the lines (look up the shortcut for commenting a block!)
# Fix the code and explore adding some more features and experiementing!

# ----------------------------------------------------------
def build_character(name, race, class_, level):
    character = {}

    # Basic Stats
    character['strength'] = 10
    character['dexterity'] = 12
    character['constitution'] = 14
    character['intelligence'] = 16
    character['wisdom'] = 10
    character['charisma'] = 12

    # Race-specific adjustments
    if race == 'human':
        character['strength'] += 1
        character['dexterity'] += 1
    elif race == 'elf':
        character['intelligence'] += 2
        character['wisdom'] += 1
    elif race == 'dwarf':
        character['constitution'] += 2
        character['wisdom'] += 1

    # Class-specific abilities
    if class_ == 'fighter':
        character['attack_bonus'] = 2
        character['armor_class'] = 18
    elif class_ == 'wizard':
        character['spellcasting_ability'] = 'intelligence'
        character['spell_slots'] = 4
    elif class_ == 'rogue':
        character['stealth_skill'] = 4
        character['sneak_attack_damage'] = 2

    # Level-specific adjustments
    if level <= 5:
        character['experience_points'] = 0
    elif level <= 10:
        character['experience_points'] = 1000
    elif level <= 15:
        character['experience_points'] = 5000
    else:
        character['experience_points'] = 20000

    # Additional features based on class and level
    if class_ == 'wizard' and level >= 10:
        character['arcane_recovery'] = True
    elif class_ == 'rogue' and level >= 15:
        character['expertise'] = ['thieves tools', 'sleight of hand']

    return character

# Example usage:
character = build_character('Eilif Stonefist', 'dwarf', 'fighter', 8)
print(character)
# ----------------------------------------------------------
