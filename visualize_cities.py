# Author: Maria Cristoforo
# Date: November 5, 2020
# Purpose: visualization of the 50 cities with largest populations on a world map

from cs1lib import *

FRAMERATE = 40
frame_counter = 0
num_city = 0
draw_once = True
# don't need a clist, can just get the populations directly, already sorted
lat_list = []
long_list = []
in_cities_population = open("cities_population.txt", "r")
for line in in_cities_population:
    s = line.strip()
    line_list = s.split(",")
    lat_list.append(float(line_list[2]))
    long_list.append(float(line_list[3]))
in_cities_population.close()



def main():
    global frame_counter, num_city, draw_once

    # use this variable so that the image is only drawn once at the beginning
    if draw_once:
        set_clear_color(1, 1, 1)
        clear()
        img = load_image("world.png")
        draw_image(img, 0, 0)
        draw_once = False

    enable_fill()


    for i in range(FRAMERATE):
        frame_counter += 1
    # keep track of the frames then can use mod operator to check how many frames have passed

    # draw a city every 600 frames in the animation
    if frame_counter % 600 == 0 and num_city <= 50:
        draw_circle((long_list[num_city] * 2) + 360, 180 - (lat_list[num_city] * 2), 3)
        num_city = num_city + 1


start_graphics(main, framerate=FRAMERATE, width=720, height=360)

