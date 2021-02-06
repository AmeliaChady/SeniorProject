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

:returns index of found interval
'''
def p(interval_list, index):
	interval = interval_list[index]
	current = index - 1
	while current > -1:
		current_interval = interval_list[current]
		if current_interval.end < interval.start:
			return current
		current -= 1
	return -1


'''
Weighted Interval Scheduling - Recursive

Takes in a list of intervals ordered least to greatest in end times
Returns a list of the subset of intervals with the greatest weight and no overlap.

'''
def WIS_R_inner(interval_list, index):
	if index < 0:
		return 0
	elif interval_list[index].weight == 0:
		return 0
	return max(
		interval_list[index].weight + WIS_R_inner(interval_list, p(interval_list, index)),
		WIS_R_inner(interval_list, index - 1))

def WIS_R(interval_list):
	return WIS_R_inner(interval_list, len(interval_list)-1)



def WIS_RM(interval_list):
	pass

def WIS_L(interval_list):
	pass

