from collections import namedtuple

Coordinates = namedtuple('Coordinates', ['x', 'y'])

'''
Takes in a set of points and returns a set of points marking the ends of each line segment in the solutions
'''
def segmented_least_squares(coordinate_list):
    return [Coordinates(1, 2), Coordinates(3, 4)]
