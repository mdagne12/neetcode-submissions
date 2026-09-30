"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # Potential edge cases: 
        # empty list or only one meeting -> short circuit to True
        # a meeting that ends at the same time that another meeting starts -> not a conflict
        # invalid meeting: negative times, or start time > end time, start time == end time (assume input is valid)

        # [1, 2], [3,4], [5, 6] -> return True
        # [1, 2], [2, 3] -> True
        # [-2, -1] or [8, 3] or [5, 5]

        intervals.sort(key = lambda i: i.start)

        for i in range(len(intervals) - 1):
            start_1, end_1 = intervals[i].start, intervals[i].end
            start_2, end_2 = intervals[i + 1].start, intervals[i + 1].end

            if start_2 < end_1:
                return False

        return True 

        