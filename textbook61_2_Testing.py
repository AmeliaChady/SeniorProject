from textbook61_2 import *

'''
really basic tests as it's more about the idea
'''

'''
make list of intervals and print it out
'''

intervals = []
print("Interval:   1-4, Weight 8")
intervals.append(Interval(1, 4, 8))

print("Interval:   2-5, Weight 3")
intervals.append(Interval(2, 5, 3))

print("Interval:   6-8, Weight 1")
intervals.append(Interval(6, 8, 1))

print("Interval:  7-11, Weight 2")
intervals.append(Interval(7, 11, 2))

print("Interval: 12-13, Weight 6")
intervals.append(Interval(12, 13, 6))

print("Interval: 10-13, Weight 4")
intervals.append(Interval(10, 13, 4))

print("Interval: 13-16, Weight 9")
intervals.append(Interval(13, 16, 9))

print("Interval: 10-20, Weight 1")
intervals.append(Interval(10, 20, 1))

print("Interval: 16-25, Weight 6")
intervals.append(Interval(16, 25, 6))

print("Interval: 22-26, Weight 6")
intervals.append(Interval(22, 26, 6))

print("Weighted Interval Scheduling")
print("Recursive")
print(WIS_R(intervals))

print("Recursive w/ Memoization")
print(WIS_RM(intervals))

print("Linear")
print(WIS_L(intervals))


