"""
Programmer: Ben Quiñones
Task: Begin a Python program that will write code that draws the sky, the ground, and clouds.
Purpose: This will help you demonstrate your ability write functions with parameters and call those functions with arguments.
"""
import tkinter as tk
import math
import random as r

print()
###############
## BEGINNING ##
###############

def main():
    width = 800
    height = 500

    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()

def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    #
    draw_sky(canvas, 0, 0)
    draw_ground(canvas, 0, 400)

    z = False
    while z == False:
        try:
            ray_count = int(input("How many rays do you want on the sun? (Whole numbers only): "))
            z = True
        except ValueError:
            print()
            print("Please enter in a whole number!")
            print()
    
    position = input("Where would you like the sun? (LEFT, CENTER or RIGHT): ")
    if position.upper() == "RIGHT":
        draw_sun(canvas, 675, 50, scale=.75, ray_count=ray_count)
    elif position.upper() == "LEFT":
        draw_sun(canvas, 50, 50, scale=.75, ray_count=ray_count)
    elif position.upper() == "CENTER":
        draw_sun(canvas, 350, 50, scale=.75, ray_count=ray_count)
    else:
        print("You did not pick a valid option. Left chosen as default.")
        draw_sun(canvas, 50, 50, scale=.75, ray_count=ray_count)
    
    z = False
    while z == False:
        try:
            cloud_count = int(input("How many clouds do you want? (Whole numbers only): "))
            z = True
        except ValueError:
            print()
            print("Please enter in a whole number!")
            print()
    
    while cloud_count != 0:
        draw_cloud(canvas, r.randint(0,800), r.randint(0,125))
        cloud_count = cloud_count - 1

    z = False
    while z == False:
        try:
            tree_count = int(input("How many trees do you want? (Whole numbers only): "))
            z = True
        except ValueError:
            print()
            print("Please enter in a whole number!")
            print()

    while tree_count != 0:
        tree_center = r.randint(0,800)
        tree_height = r.randint(100,180)
        draw_pine_tree(canvas, tree_center, 250 + (150 - tree_height), tree_height)
        tree_count = tree_count - 1

    z = False
    while z == False:
        try:
            grass_count = int(input("How many blades of grass do you want? (Whole numbers only): "))
            z = True
        except ValueError:
            print()
            print("Please enter in a whole number!")
            print()

    while grass_count != 0:
        draw_grass(canvas, r.randint(0,800), r.randint(398,496))
        grass_count = grass_count - 1

    #draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 100)
    #

def draw_sky(canvas, sky_left, sky_top):
    #
    sky_width = 800
    sky_height = 500
    sky_right = sky_left + sky_width
    sky_bottom = sky_top + sky_height

    canvas.create_rectangle(sky_left, sky_top, sky_right, sky_bottom, fill="#A7FBFF")
    #

def draw_ground(canvas, ground_left, ground_top):
    #
    ground_width = 800
    ground_height = 500
    ground_right = ground_left + ground_width
    ground_bottom = ground_top + ground_height

    canvas.create_rectangle(ground_left, ground_top, ground_right, ground_bottom, fill="#824D00")
    #

def draw_cloud(canvas, cloud_left, cloud_top, scale=1):
    cloud_width = 100 * scale
    cloud_height = 100 * scale
    cloud_right = cloud_left + cloud_width
    cloud_bottom = cloud_top + cloud_height

    canvas.create_oval(cloud_left, cloud_top, cloud_right, cloud_bottom, fill="#E4E4E4", width=False)

def draw_grass(canvas, grass_left, grass_top):
    grass_width = 8
    grass_height = 20
    grass_right = grass_left + grass_width
    grass_bottom = grass_top + grass_height

    canvas.create_arc(grass_left, grass_top, grass_right, grass_bottom, fill="#00B050", width=False)

def draw_sun(canvas, sun_left, sun_top, scale=1, ray_count=10):
    #
    sun_width = 100 * scale
    sun_height = 100 * scale
    ray_length = 100 * scale
    ray_width = 3 * scale

    sun_right = sun_left + sun_width
    sun_bottom = sun_top + sun_height
    sun_center_x = sun_left + (sun_width / 2)
    sun_center_y = sun_top + (sun_height / 2)

    canvas.create_oval(sun_left, sun_top, sun_right, sun_bottom, fill="#FFFF00", width=False)
    
    for i in range(ray_count):
        angle = ((2 * math.pi) / ray_count) * i
        ray_x = sun_center_x + math.cos(angle) * ray_length
        ray_y = sun_center_y + math.sin(angle) * ray_length
        canvas.create_line(sun_center_x, sun_center_y, ray_x, ray_y, width=3, fill="#FFFF00")

    #

def draw_grid(canvas, left, top, right, bottom, grid_spacing):
    text_horizontal_margin = 20
    text_vertical_margin = 10

    for i in range(top, bottom, grid_spacing):
        canvas.create_line(left, i, right, i)
        canvas.create_text(left + text_horizontal_margin, i + text_vertical_margin, text=f"{i}")
    
    for i in range(left, right, grid_spacing):
        canvas.create_line(i, top, i, bottom)
        canvas.create_text(i, top + text_vertical_margin, text=f"{i}")

def draw_pine_tree(canvas, peak_x, peak_y, height):
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")

main()

#########
## END ##
#########
print()