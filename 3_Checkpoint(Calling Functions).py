"""
Programmer: Ben Quiñones
Task: Write a basic program using inputs and outputs.
Purpose: This will help you demonstrate your understanding of decisions (if statements) and logic.
"""
print()
###############
## BEGINNING ##
###############

number_items = float(input("Enter the amount of items: "))
box_space = float(input("Enter the amount of items per box: "))

box_number = number_items / box_space

print()
print(f"For {number_items:.0f} items, with a limit of {box_space} items per box, you will need {round(box_number)} box(es). ")

#########
## END ##
#########
print()