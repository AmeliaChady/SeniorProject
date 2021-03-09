from SegmentedLeastSquares_CreatePoints import *
from SegmentedLeastSquares import *

print("\nLinear Points")
coordinates = segmented_least_squares(create_linear_points())
for coord in coordinates:
    print(str(round(coord.x, 2)) + "\t" + str(round(coord.y, 2)))

print("\nSplit Points")
coordinates = segmented_least_squares(create_split_points())
for coord in coordinates:
    print(str(round(coord.x, 2)) + "\t" + str(round(coord.y, 2)))

print("\nDouble Split Points")
coordinates = segmented_least_squares(create_double_split_points())
for coord in coordinates:
    print(str(round(coord.x, 2)) + "\t" + str(round(coord.y, 2)))

print("\nNon Whole Numbers")
coordinates = segmented_least_squares(create_non_whole_points())
for coord in coordinates:
    print(str(round(coord.x, 2)) + "\t" + str(round(coord.y, 2)))
