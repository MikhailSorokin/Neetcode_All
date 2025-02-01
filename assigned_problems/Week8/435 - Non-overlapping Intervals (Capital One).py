class Solution:
    # Rodrigo
    # https://leetcode.com/problems/non-overlapping-intervals/?envType=company&envId=capital-one&favoriteSlug=capital-one-six-months
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x:x[1])

        prev_end = float('-inf')
        #non_overlapping_count = 0
        overlapping_count = 0
        #res = [intervals[0]]
        ptr = 0
        #n = len(intervals)
        while ptr < len(intervals):
            start, end = intervals[ptr]
            interval = intervals[ptr]
            if start >= prev_end:
                prev_end = end
                #res.append(intervals[i])
                ptr += 1
            else:
                overlapping_count += 1
                intervals.remove(interval)
                #Don't increment pointer

        #print(f'{intervals}')
        return overlapping_count
