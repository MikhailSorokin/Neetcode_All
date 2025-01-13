"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:

    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        if len(schedule) == 0:
            return 0

        intervals = []
        for i in range(0, len(schedule)):
            for j in range(0, len(schedule[i])):
                intervals.append((schedule[i][j].start, schedule[i][j].end))

        # Sort by key start
        intervals.sort(key=lambda x: x[0])

        print(intervals)

        prev = intervals[0]
        results = []
        nextRight = intervals[0][1]
        for interval in intervals[1:]:
            prev_start, prev_end = prev
            start, end = interval
            
            if start > nextRight:
                results.append(Interval(nextRight, start))
            prev = interval
            nextRight = max(nextRight, end, prev_end)

        return results