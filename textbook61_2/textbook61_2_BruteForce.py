from textbook61_2 import *
from itertools import combinations

'''
Returns true if there is no overlap between intervals
'''
def is_possible(intervals):
    for x in range(len(intervals)-1):
        interval_x = intervals[x]
        for y in range(x+1, len(intervals)):
            interval_y = intervals[y]
            if not (interval_y.end < interval_x.start or
                    interval_y.start > interval_x.end):
                return False
    return True

def brute_force_WIS(intervals):
    max_weight = 0
    max_intervals = []

    for x in range(1, len(intervals)):
        sets = combinations(intervals, x)
        for interval_set in sets:
            if is_possible(interval_set):
                total_sum = 0
                for interval in interval_set:
                    total_sum += interval.weight
                if total_sum > max_weight:
                    max_weight = total_sum
                    max_intervals = interval_set

    return max_intervals, max_weight
