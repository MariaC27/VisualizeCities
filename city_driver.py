# Author: Maria Cristoforo
# Date: October 28, 2020
# Purpose: parse the world_cities file and create a list of cities, then write that to another text file

from VisualizeCities.city import City



# for testing file parsing only

in_world_cities = open("world_cities.txt", "r")
clist = [] # the list to store all the cities
for line in in_world_cities:
    s = line.strip()
    line_list = s.split(",")
    c = City(line_list[0], line_list[1], line_list[2], int(line_list[3]), float(line_list[4]), float(line_list[5]))
    clist.append(c)

in_world_cities.close()


# testing if reading the file worked correctly
# for i in clist:
#     print(i)


# now writing to the new file
cities_out = open("cities_out.txt", "w")
for i in clist:
    cities_out.write(str(i) + "\n")

cities_out.close()

