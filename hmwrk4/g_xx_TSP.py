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


class City(object):
    """
    Represent a city in the tour and must store the distances to the other cities.
    """
    def __init__(self, oslo=None, bergen=None, stavanger=None, trondheim=None, kristiansand=None):
        self.oslo = oslo
        self.bergen = bergen
        self.stavanger = stavanger
        self.trondheim = trondheim
        self.kristiansand = kristiansand

    def distanceTo(self, destination):
        """
        Takes a specific destination as an argument and returns the distance to that specific destination.
        :param destination:
        :return:
        """
        if destination.casefold() is 'oslo':
            return self.oslo
        elif destination.casefold() is 'bergen':
            return self.bergen
        elif destination.casefold() is 'stavanger':
            return self.stavanger
        elif destination.casefold() is 'trondheim':
            return self.trondheim
        elif destination.casefold() is 'kristiansand':
            return self.kristiansand
        else:
            return -1


class Tour(object):
    def __init__(self):
        self.cities = {}

    def __add__(self, city, dist_oslo=None, dist_bergen=None, dist_stavanger=None,
                dist_trondheim=None, dist_kristiansand=None):
        self.cities[city] = City(oslo=dist_oslo, bergen=dist_bergen, stavanger=dist_stavanger,
                                 trondheim=dist_trondheim, kristiansand=dist_kristiansand)

    def addCity(self):
        """
        Allow the user to add a city to the tour.
        :return:
        """
        # ISSUE: Does not loop over dict to check what cities is present in tour.
        print("\nEnter the information of the city you'd like to add")
        city = input('City: ')
        dist_oslo = input('Distance to Oslo: ')
        dist_bergen = input('Distance to Bergen: ')
        dist_stavanger = input('Distance to Stavanger: ')
        dist_trondheim = input('Distance to Trondheim: ')
        dist_kristiansand = input('Distance to Kristiansand: ')

        self.cities[city] = City(oslo=dist_oslo, bergen=dist_bergen, stavanger=dist_stavanger,
                                 trondheim=dist_trondheim, kristiansand=dist_kristiansand)
        print("\n# City added")

    def findTour(self):
        """
        Find a tour and return the order of the cities to visit and the total distance.
        :return:
        """
        return


def main():
    sandy_boy_prestige_tours = Tour()
    sandy_boy_prestige_tours.__add__('Oslo', dist_bergen=6.47, dist_stavanger=7.10,
                                     dist_trondheim=6.10, dist_kristiansand=3.56)
    sandy_boy_prestige_tours.__add__('Bergen', dist_oslo=7.14, dist_stavanger=4.42,
                                     dist_trondheim=9.30, dist_kristiansand=7.39)
    sandy_boy_prestige_tours.__add__('Stavanger', dist_oslo=7.00, dist_bergen=4.48,
                                     dist_trondheim=13.37, dist_kristiansand=3.14)
    sandy_boy_prestige_tours.__add__('Trondheim', dist_oslo=6.24, dist_bergen=9.34,
                                     dist_stavanger=13.36, dist_kristiansand=10.12)
    sandy_boy_prestige_tours.__add__('Kristiansand', dist_oslo=4.30, dist_bergen=7.45,
                                     dist_stavanger=3.33, dist_trondheim=10.17)

    while True:
        selection = input("""

    ----MAIN MENU----
    1: Add city
    2: Find tour
    3: Explode into oblivion

    Please enter your choice: """)

        if selection == '1':
            sandy_boy_prestige_tours.addCity()
        elif selection == '2':
            sandy_boy_prestige_tours.findTour()
        elif selection == '3':
            print('# BOOM!')
            return False
        else:
            print('\n# 404 - Page cannot be found')


main()
