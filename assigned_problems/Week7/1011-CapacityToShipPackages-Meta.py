class Solution:
    # Meta - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
    def isFeasible(self, weights, capacity, days):
        daysNeeded = 1
        currentLoad = 0
        for weight in weights:
            currentLoad += weight
            if currentLoad > capacity:
                daysNeeded += 1
                currentLoad = weight

        return daysNeeded <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        totalLoad = 0
        maxLoad = 0
        for weight in weights:
            totalLoad += weight
            maxLoad = max(maxLoad, weight)

        l = maxLoad
        r = totalLoad

        while l < r:
            mid = (l + r) // 2
            if self.isFeasible(weights, mid, days):
                r = mid
            else:
                l = mid + 1

        return l
        