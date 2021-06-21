"""
Programmer: Ben Quiñones
Task: Write a simple Python program.
Purpose: This will help you demonstrate your understanding of input, variables, arithmetic, and output.
"""
"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum.
"""
print()
###############
## BEGINNING ##
###############

age = int(input("Please enter your age: "))
heart_max = 220 - age

print(f"When you exercise to strengthen your heart, you should \n"
f"keep your heart rate between {heart_max * .65:.0f} and {heart_max * .85:.0f} beats per minute")

#########
## END ##
#########
print()