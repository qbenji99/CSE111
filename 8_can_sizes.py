"""
Programmer: Ben Quiñones
Task: Begin a Python program that will write code that draws the sky, the ground, and clouds.
Purpose: This will help you demonstrate your ability write functions with parameters and call those functions with arguments.
"""
print()
###############
## BEGINNING ##
###############
import math as m

def main():
    #
    names = []
    radius = []
    heights = []
    cost = []
  
    with open("data.csv") as data:
        data.readline()
        for line in data:
        #
        partstrip = line.strip()
        part = partstrip.split(",")

        names.append(part[0])
        radius.append(float(part[1]))
        heights.append(float(part[2]))
        cost.append(float(part[3]))
        #

    for i in range(len(radius)):
        #
        cyl_volume = cylinder_volume(radius[i], heights[i])
        cyl_surf_area = cylinder_surf_area(radius[i],heights[i])
        storage = storage_efficiency(cyl_volume, cyl_surf_area)
        print(f"{names[i]} , {storage:.1f}")
        #
    #


def cylinder_volume(radius, height):
    #
    volume = m.pi * (radius ** 2) * height
    return volume
    #


def cylinder_surf_area(radius, height):
    #
    surface_area = 2 * (m.pi) * radius * (radius + height)
    return surface_area
    #


def storage_efficiency(volume, surface_area):
    #
    storage_efficiency = volume / surface_area
    return storage_efficiency
    #

main()


#########
## END ##
#########
print()