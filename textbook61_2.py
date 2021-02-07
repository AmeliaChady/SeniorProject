from collections import namedtuple

'''
start (int)- start time of the interval 
end (int)- end time of the interval
weight (int)- importance of the interval
'''
Interval = namedtuple('Interval', ['start', 'end', 'weight'])

'''
gets interval test set and also prints it out
'''
def test_intervals():
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
	
	return intervals


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



def WIS_RM_inner(interval_list, index, memo):
	if index < 0:
		return 0
	elif memo[index] is not None:
		return memo[index]
	elif interval_list[index].weight == 0:
		return 0
	memo[index] = interval_list[index].weight + WIS_RM_inner(interval_list, p(interval_list, index), memo)
	index_minus_1 = WIS_RM_inner(interval_list, index - 1, memo)
	return max(memo[index], index_minus_1)

def WIS_RM(interval_list):
	memo = [None]*len(interval_list)
	ans = WIS_RM_inner(interval_list, len(interval_list)-1, memo)
	return ans

def WIS_L(interval_list):
	pass

