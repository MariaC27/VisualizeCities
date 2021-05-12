# Author: Maria Cristoforo
# Date: October 28, 2020
# Purpose: the City class


class City:

    def __init__(self, code, name, region, p, lat, long):
        self.code = code
        self.name = name
        self.region = region
        self.population = p
        self.lat = lat
        self.long = long

    def __str__(self):
        # string consisting of the city’s name, population, latitude, and longitude
        return self.name + "," + str(self.population) + "," + str(self.lat) + "," + str(self.long)


