from collections import namedtuple

Coordinates = namedtuple('Coordinates', ['x', 'y'])
Line = namedtuple('Line', ['a', 'b'])


def least_squares(coordinate_list):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_xsq = 0
    n = len(coordinate_list)

    for i in range(n):
        coord = coordinate_list[i]
        sum_x += coord.x
        sum_y += coord.y
        sum_xy += coord.x * coord.y
        sum_xsq += coord.x ** 2

    a = (n * sum_xy - sum_x * sum_y)/(n * sum_xsq - sum_x ** 2)
    b = (sum_y - a * sum_x)/n
    return Line(a, b)


def least_squares_error(coordinate_list, line):
    error = 0
    for i in range(len(coordinate_list)):
        coord = coordinate_list[i]
        error += (coord.y - line.a * coord.x - line.b)**2
    return error


'''
Takes in a set of points and returns a set of points marking the ends of each line segment in the solutions
'''
def segmented_least_squares(coordinate_list):
    line = least_squares(coordinate_list)
    start_coords = Coordinates(coordinate_list[0].x, line.a * coordinate_list[0].x + line.b)
    end_coords = Coordinates(coordinate_list[-1].x, line.a * coordinate_list[-1].x + line.b)
    return [start_coords, end_coords]



