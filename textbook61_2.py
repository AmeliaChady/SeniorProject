from collections import namedtuple

'''
start (int)- start time of the interval 
end (int)- end time of the interval
weight (int)- importance of the interval
'''
Interval = namedtuple('Interval', ['start', 'end', 'weight'])


'''
In the list of intervals, finds the interval that has its end time closest to the start time of the interval at index.
Note: In event of ties, the higher index is picked.
Note: Assumes list is ordered least to greatest in end times.

interval_list: intervals to look through
index: the index the interval to check against is stored in. 
'''
def p(interval_list, index):
	pass


'''
Weighted Interval Scheduling - Recursive

Takes in a list of intervals ordered least to greatest in end times
Returns a list of the subset of intervals with the greatest weight and no overlap.

'''
def WIS_R_inner(interval_list, index):
	pass

def WIS_R(interval_list):
	pass



def WIS_RM(interval_list):
	pass

def WIS_L(interval_list):
	pass

