class Solution:

    # Working Saman + Mike Solution
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        overlap_indices = []
        for index, tup in enumerate(intervals):
            # Now, add overlapping indices
            if tup[0] <= newInterval[0] <= tup[1] or tup[0] <= newInterval[1] <= tup[1] or \
                newInterval[0] <= tup[0] and tup[1] <= newInterval[1]:
                overlap_indices.append(index)
            if tup[0] > newInterval[1] and not overlap_indices:
                # If no overlap, add at that point and return
                intervals.insert(index, newInterval)
                return intervals

        if not overlap_indices:
            intervals.append(newInterval)
            return intervals

        # Now merge and remove all besides last point in overlapping
        least = intervals[overlap_indices[0]]
        greatest = intervals[overlap_indices[len(overlap_indices) - 1]]
        insert_index = overlap_indices[0]

        del intervals[overlap_indices[0]:overlap_indices[len(overlap_indices) - 1] + 1]
        intervals.insert(insert_index, [min(least[0], newInterval[0]), max(greatest[1], newInterval[1])])
        return intervals
        
    # Easier to understand solution
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = 0
        while index < len(intervals):
            tup = intervals[index]
            # Check if before or after interval 
            if tup[0] > newInterval[1]:
                # Interval is bigger than newInterval. No overlap. Insert now
                intervals.insert(index, newInterval)
                return intervals
            elif newInterval[0] > tup[1]:
                index += 1
            else:
                # OVERLAP
                newInterval = [min(tup[0], newInterval[0]), max(tup[1], newInterval[1])]
                del intervals[index]

        intervals.append(newInterval)
        return intervals
        
    # Most efficient on leetcode
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)
        return res


