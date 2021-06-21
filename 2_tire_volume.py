"""
Programmer: Ben Quiñones
Task: Write a program with inputs and outputs.
Purpose: This will help you prove that you can write a simple Python program that gets input and displays output.
"""
"""
The size of a car tire in the United States is represented with three numbers like this: 205/60R15. 
The first number is the width of the tire in millimeters. 
The second number is the aspect ratio. 
The third number is the diameter in inches of the wheel that the tire fits.

v is the volume in milliliters,
π is the constant PI, the ratio of the circumference divided by the diameter of a circle (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
"""
import math
from datetime import datetime

print()
###############
## BEGINNING ##
###############

current_date_and_time = datetime.now()
current_date = current_date_and_time.date()
answer = "NO"

while answer.upper() != "YES":
    width = float(input("Enter the width of the tire in mm: "))
    aspect_ratio = float(input("Enter the aspect ratio of the tire in mm: "))
    diameter = float(input("Enter the diameter of the tire in inches: "))
    volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000

    print()
    print("The approximate volume of the wheel is...")
    print()
    print(f"~{volume:.1f} in milliliters")
    print(f"~{volume / 1000:.1f} in liters")
    print(f"~{(volume / 1000) / 3.785:.1f} in gallons")

    print()
    with open("volumes.txt", "at") as volumes_file:
        print(f"{current_date}, {width}, {aspect_ratio}, {volume:.1f} milliliters", file=volumes_file)
        print(f"{current_date}, {width}, {aspect_ratio}, {volume / 1000:.1f} liters", file=volumes_file)
        print(f"{current_date}, {width}, {aspect_ratio}, {volume / 1000 / 3.785:.1f} gallons", file=volumes_file)
        print("", file=volumes_file)
    
    answer = input("Are you done measuring tire volume? (YES or NO): ")
    print()


#########
## END ##
#########
print()