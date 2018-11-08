'''
Table 1: Distances between cities. The table shows the traveling distance from the on the left
margin to the city on the top margin. Note that the table is not symmetric.

                Oslo    Bergen  Stavanger   Trondheim   Kristiansand
Oslo            -       6.47    7.10        6.10        3.56
Bergen          7.14    -       4.42        9.30        7.39
Stavanger       7       4.48    -           13.37       3.14
Trondheim       6.24    9.34    13.36       -           10.12
Kristiansand    4.3     7.45    3.33        10.17       -
'''

distance_matrix = [
        [0, 6.47, 7.10, 6.10, 3.56],
        [7.14, 0, 4.42, 9.30, 7.39],
        [7, 4.48, 0, 13.37, 3.14],
        [6.24, 9.34, 13.36, 0, 10.12],
        [4.3, 7.45, 3.33, 10.17, 0]
        ]

class City(object):
    """
    Represent a city in the tour and must store the distances to the other cities.
    """
    def __init__(self, index, name):
        self.index = index
        self.name = name

    def __str__(self):
        return self.name

    def distanceTo(self, city):
        """
        Takes a specific destination as an argument and returns the distance to that specific destination.
        :param destination:
        :return:
        """
        return distance_matrix[self.index][city.index]


class Tour(object):
    def __init__(self):
        self.cities = []

    def addCity(self, city):
        """
        Allow the user to add a city to the tour.
        :return:
        """
        self.cities.append(city)

    def findTour(self, city):
        """
        Find a tour and return the order of the cities to visit and the total distance.
        :return:
        """
        print('')
        tour_cities = self.cities # 1. A candidate set, from which a solution is created
        travel_path = [city]
        travel_distance = 0
        nr_of_cities_to_visit = len(tour_cities)

        while nr_of_cities_to_visit > 1:
            tour_cities.remove(city)
            nr_of_cities_to_visit -= 1
            next_city = tour_cities[0] # 2. A selection function, which chooses the best candidate to be added to the solution
            distance_next_city = city.distanceTo(next_city)

            for i in range(0, nr_of_cities_to_visit):
                distance = city.distanceTo(tour_cities[i])
                if distance < distance_next_city: # 3. A feasibility function, that is used to determine if a candidate can be used to contribute to a solution
                    next_city = tour_cities[i]
                    distance_next_city = distance

            travel_path.insert(len(travel_path), next_city) # 4. An objective function, which assigns a value to a solution, or a partial solution
            travel_distance += distance_next_city
            print('# {} added to travel path.'.format(next_city))
            city = next_city

        travel_path.insert(len(travel_path), travel_path[0]) # 5. A solution function, which will indicate when we have discovered a complete solution
        travel_distance += city.distanceTo(travel_path[0])

        print('\nTRAVEL PATH:')
        for i in range(0, len(travel_path)):
            print(travel_path[i])

        print('\nTRAVEL DISTANCE: ' + str(travel_distance))


def main():
    oslo = City(0, 'Oslo')
    bergen = City(1, 'Bergen')
    stavanger = City(2, 'Stavanger')
    trondheim = City(3, 'Trondheim')
    kristiansand = City(4, 'Kristiansand')

    charter = Tour()
    charter.addCity(oslo)
    charter.addCity(bergen)
    charter.addCity(stavanger)
    charter.addCity(trondheim)
    charter.addCity(kristiansand)

    while True:
        selection = input("""

    ----MAIN MENU----
    1: Find tour starting in Oslo
    2: Find tour starting in Bergen

    Please enter your choice: """)

        if selection == '1':
            charter.findTour(oslo)
            return False
        elif selection == '2':
            charter.findTour(bergen)
            return False
        else:
            print('\n# 404 - Page cannot be found')


main()
