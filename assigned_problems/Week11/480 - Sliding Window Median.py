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
from typing import List

class MaxHeapItem:
  def __init__(self, val): self.val = val
  def __lt__(self, other): return self.val > other.val
  def __eq__(self, other): return self.val == other.val
  def __str__(self): return str(self.val)

class DualHeap:
    def __init__(self, k):
        # max heap for the smaller half of the input
        self.small = []
        # min heap for the larger half of the input
        self.large = []
        # used to track the count of numbers that should be removed later
        self.lazy = collections.defaultdict(int)
        
        self.k = k

        # current size of each heap, excluding the elements marked for deletion
        self.small_size = 0
        self.large_size = 0

    def addNum(self, num: int) -> None:
        # add to small first, since we want small > large in case of k being odd
        if not self.small or num <= self.small[0].val:
            heappush(self.small, MaxHeapItem(num))
            self.small_size += 1
        else:
            heappush(self.large, num)
            self.large_size += 1
        self.balance()

    def removeNum(self, num):
        """
        mark number for lazy deletion
        """
        self.lazy[num] += 1
        if num <= self.small[0].val:
            self.small_size -= 1
            if num == self.small[0].val:
                # the lazy deleted value has reached the top of the heap, time to remove
                self.prune(self.small)
        else:
            self.large_size -= 1
            if num == self.large[0]:
                self.prune(self.large)
        # maintain balance after adding/removing items
        self.balance()

    def balance(self):
        """
        ensures two heaps have proper size balance
        """
        # we want small == large when k is even and small == large + 1 if k is odd
        if self.small_size > self.large_size + 1: # small heap is too big
            # ensure the top of the heap is not an element marked for deletion
            self.prune(self.small)
            # item that needs to be mvoe to large heap
            item = heappop(self.small)
            # decrement size of non-soft deleted elements in small heap
            self.small_size -= 1
            heappush(self.large, item.val)
            self.large_size += 1
        elif self.small_size < self.large_size:
            # same thing as above, but in reverse, large heap is too big
            self.prune(self.large)
            val = heappop(self.large)
            item = MaxHeapItem(val)
            self.large_size -= 1
            heappush(self.small, item)
            self.small_size += 1


    def prune(self, heap):
        # ensure the number on the top of the heap is not a number marked for lazy deletion
        # prune before we balance, and prune after marking an element for lazy removal, if that element has reached the top of the
        # heap from which it was removed
        while heap:
            num = heap[0] if heap is self.large else heap[0].val
            if self.lazy[num] > 0:
                heappop(heap)
                self.lazy[num] -= 1
            else:
                break
    
    def get_median(self):
        # prune lazy removed before getting median
        self.prune(self.small)
        self.prune(self.large)
        if self.small_size == self.large_size:
            return (self.large[0] + self.small[0].val) / 2.0
        else:
            return float(self.small[0].val)


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k == 1:
            return [float(num) for num in nums]

        medianFinder = DualHeap(k)
        allMedians = []

        for i in range(k):
            medianFinder.addNum(nums[i])

        allMedians.append(medianFinder.get_median())

        for i in range(k, len(nums)):
            medianFinder.addNum(nums[i])  # Add the new element
            medianFinder.removeNum(nums[i - k])  # Remove the outgoing element
            allMedians.append(medianFinder.get_median())

        return allMedians