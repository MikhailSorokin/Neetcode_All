import heapq

class Solution:
    # Mike
    # Part One
    # https://leetcode.com/problems/find-median-from-data-stream/description/
    class MedianFinder:

    def __init__(self):
        self.maxHeap = [] # Maximum of left side
        self.minHeap = [] # Minimum of right side

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -1 * num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * val) 

        print(f'Maxheap: {self.maxHeap}')
        print(f'Minheap: {self.minHeap}')
        print("\n")

    def findMedian(self) -> float:
        n = len(self.maxHeap)
        m = len(self.minHeap)
        totalLen = n + m
        if totalLen % 2 != 0:
            if n > m:
                return -1 * self.maxHeap[0]
            else:
                return self.minHeap[0]
        else:
            return (self.minHeap[0] + (-1 * self.maxHeap[0])) / 2.0
        
            


    # Your MedianFinder object will be instantiated and called as such:
    # obj = MedianFinder()
    # obj.addNum(num)
    # param_2 = obj.findMedian()
    
    # Part Two
    # https://leetcode.com/problems/sliding-window-median/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        