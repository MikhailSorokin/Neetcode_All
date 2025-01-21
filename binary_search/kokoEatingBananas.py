class Solution:
    
    # Rodrigo
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        totalTime = 0
        res = 0
        while left <= right:
            mid = (left + right) // 2

            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / mid)

            if totalTime <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
            #print("Total time: ", totalTime)
            #print("Left: ", left, ", right: ", right)
            
    return res
    
    # Mike
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        totalTime = 0
        while left <= right:
            mid = (left + right) // 2

            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / mid)

            if totalTime <= h:
                right = mid - 1
            else:
                left = mid + 1
        
            #print("Total time: ", totalTime)
            #print("Left: ", left, ", right: ", right)


        return left