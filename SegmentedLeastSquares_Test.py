from SegmentedLeastSquares_CreatePoints import *
from SegmentedLeastSquares import *

print("\nLinear Points")
coordinates = segmented_least_squares(create_linear_points())
for coord in coordinates:
    print(str(coord.x) + "\t" + str(coord.y))

print("\nSplit Points")
coordinates = segmented_least_squares(create_split_points())
for coord in coordinates:
    print(str(coord.x) + "\t" + str(coord.y))

print("\nDouble Split Points")
coordinates = segmented_least_squares(create_double_split_points())
for coord in coordinates:
    print(str(coord.x) + "\t" + str(coord.y))

print("\nNon Whole Numbers")
coordinates = segmented_least_squares(create_non_whole_points())
for coord in coordinates:
    print(str(coord.x) + "\t" + str(coord.y))
