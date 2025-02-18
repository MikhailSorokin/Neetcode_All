class Solution:
    # Rodrigo
    # https://leetcode.com/problems/number-of-flowers-in-full-bloom/?envType=company&envId=capital-one&favoriteSlug=capital-one-all
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = sorted([start for start, _ in flowers])
        ends = sorted([end for _, end in flowers])

        res = []
        for t in people:

            started = bisect_right(starts,t)

            ended = bisect_left(ends, t)

            res.append(started - ended)
        return res
