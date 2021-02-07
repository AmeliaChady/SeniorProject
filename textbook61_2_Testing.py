from textbook61_2 import *
from textbook61_2_BruteForce import *

'''
really basic tests as it's more about the idea
'''

intervals = test_intervals()

print("Weighted Interval Scheduling")
print("Gotten From Brute Force: ")
brute_force = brute_force_WIS(intervals)
print(brute_force[0])
print(brute_force[1])

print("Recursive")
print(WIS_R(intervals))

print("Recursive w/ Memoization")
print(WIS_RM(intervals))

print("Linear")
print(WIS_L(intervals))


