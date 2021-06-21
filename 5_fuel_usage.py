"""
Programmer: Ben Quiñones
Task: Write a basic program using inputs and outputs.
Purpose: This will help you demonstrate your understanding of decisions (if statements) and logic.
"""
print()
###############
## BEGINNING ##
###############
def main():
    end = 0
    start = 0
    gallons = 0
    mpg = 0
    lp100k = 0
    # ^ Variables ^ #
    #################

    start = int(input("Enter the first odometer reading (in miles): "))
    end = int(input("Enter the second odometer reading (in miles): "))
    gallons = float(input("Enter the amount of fuel used (in gallons): "))
    mpg = miles_per_gallon(start, end, gallons)
    lp100k = lp100k_from_mpg(mpg)

    print(f"{mpg:.1f} miles per gallon")
    print(f"{lp100k:.2f} liters per 100 kilometers")
    
    pass

def miles_per_gallon(start_miles, end_miles, amount_gallons):
    mpg = (end_miles - start_miles) / amount_gallons
    # ^ Variables ^ #
    #################

    return mpg

def lp100k_from_mpg(mpg):
    lp100k = 235.215 / mpg
    "(lp100k) is Liters per 100 kilometers"
    # ^ Variables ^ #
    #################

    return lp100k

main()


#########
## END ##
#########
print()