"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # [5, 5], [8, 3], [-1, 0] -> no need for input validation
        # [0, 8], [8, 10] -> not conflicting only one room needed
        # input may not be sorted

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        max_num_rooms, count = 0, 0
        start_idx, end_idx = 0, 0

        while start_idx < len(start):
            if start[start_idx] < end[end_idx]:
                start_idx += 1
                count += 1
            else:
                end_idx += 1
                count -= 1

            max_num_rooms = max(max_num_rooms, count)

        return max_num_rooms
         