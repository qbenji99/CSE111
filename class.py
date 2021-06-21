import math

def main():
    # Prompt user for how many circles they have
    numberOfCircles = promptForNumberOfCircles()
    print(numberOfCircles)
    # Get area for each
    areas = loopForCircles(numberOfCircles)
    # Display the area for each

    print(areas)

def loopForCircles(numberOfCircles):
    areas = []
    for _ in range(0, numberOfCircles):
        r = promptForRadius()
        a = computeCircleArea(r)
        areas.append(a)
    return areas

def promptForRadius():
    #
    _ = False
    while _ == False:
        try:
            radius = int(input("Please enter the radius: "))
            _ = True
        except ValueError:
            print()
            print("TYPE IN AN INTEGER!!! Jeezzzzz....")
            print()
    return radius
    #

def promptForNumberOfCircles():
    num = input("Please enter the number of circles you are working with: ")
    return int(num)

def computeCircleArea(radius):
    return math.pi * radius**2

main()