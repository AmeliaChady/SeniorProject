from SegmentedLeastSquares import *


def create_linear_points():
    coordinates = []
    coordinates.append(Coordinates(1, 1))
    coordinates.append(Coordinates(3, 2))
    coordinates.append(Coordinates(3, 4))
    coordinates.append(Coordinates(4, 6))
    coordinates.append(Coordinates(5, 5))
    coordinates.append(Coordinates(6, 4))
    coordinates.append(Coordinates(8, 6))
    coordinates.append(Coordinates(8, 9))
    coordinates.append(Coordinates(9, 9))
    coordinates.append(Coordinates(10, 3))
    coordinates.append(Coordinates(11, 11))
    coordinates.append(Coordinates(11, 12))
    coordinates.append(Coordinates(13, 15))
    coordinates.append(Coordinates(14, 15))
    coordinates.append(Coordinates(15, 12))
    coordinates.append(Coordinates(12, 17))
    coordinates.append(Coordinates(17, 17))
    coordinates.append(Coordinates(16, 18))
    coordinates.append(Coordinates(19, 16))
    coordinates.append(Coordinates(20, 20))
    return coordinates


def create_split_points():
    coordinates = create_linear_points()
    coordinates.append(Coordinates(21, 26))
    coordinates.append(Coordinates(21, 29))
    coordinates.append(Coordinates(22, 29))
    coordinates.append(Coordinates(22, 33))
    coordinates.append(Coordinates(22, 36))
    coordinates.append(Coordinates(23, 35))
    coordinates.append(Coordinates(23, 40))
    coordinates.append(Coordinates(23, 43))
    coordinates.append(Coordinates(24, 40))
    coordinates.append(Coordinates(24, 45))
    return coordinates


def create_double_split_points():
    coordinates = create_split_points()
    coordinates.append(Coordinates(25, 40))
    coordinates.append(Coordinates(26, 42))
    coordinates.append(Coordinates(27, 41))
    coordinates.append(Coordinates(28, 41))
    coordinates.append(Coordinates(29, 40))
    coordinates.append(Coordinates(30, 44))
    coordinates.append(Coordinates(31, 39))
    coordinates.append(Coordinates(32, 41))
    coordinates.append(Coordinates(33, 40))
    coordinates.append(Coordinates(34, 43))
    return coordinates


def create_non_whole_points():
    coordinates = []
    coordinates.append(Coordinates(-1, -1.5))
    coordinates.append(Coordinates(0, 0))
    coordinates.append(Coordinates(1, 0.25))
    coordinates.append(Coordinates(3.5, 1))
    coordinates.append(Coordinates(4.1, 1.5))
    coordinates.append(Coordinates(4.3, 1.3))
    coordinates.append(Coordinates(5, 3))
    coordinates.append(Coordinates(5.5, 2))
    coordinates.append(Coordinates(6.2, 2.3))
    coordinates.append(Coordinates(7, 3))
    return coordinates
