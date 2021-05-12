# Author: Maria Cristoforo
# Date: November 4, 2020
# Purpose: sort city information according to different criteria and write into text files

from VisualizeCities.city import City
from VisualizeCities.quicksort import *

# read the cities from world_cities.txt first
in_world_cities = open("world_cities.txt", "r")
clist = [] # the list to store all the cities
for line in in_world_cities:
    s = line.strip()
    line_list = s.split(",")
    c = City(line_list[0], line_list[1], line_list[2], int(line_list[3]), float(line_list[4]), float(line_list[5]))
    clist.append(c)

in_world_cities.close()

# now we have a list of Cities called clist



# sort alphabetically
cities_alpha = open("cities_alpha.txt", "w")

sort(clist, compare_city_name)
for i in clist:
    cities_alpha.write(str(i) + "\n")
cities_alpha.close()


# sorts by population largest to smallest
cities_population = open("cities_population.txt", "w")

sort(clist, compare_city_population)
for i in clist:
    cities_population.write(str(i) + "\n")
cities_population.close()


# sorts by latitude south to north
cities_latitudes = open("cities_latitudes.txt", "w")

sort(clist, compare_city_latitude)
for i in clist:
    cities_latitudes.write(str(i) + "\n")
cities_latitudes.close()


