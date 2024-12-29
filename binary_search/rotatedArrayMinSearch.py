class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            # Check if you are at the solution
            if (right - left) == 0:
                return nums[left]
            # Check if mid is greater than last
            elif (nums[mid] > nums[right]):
                left = mid + 1
            else:
                right = mid

        return -1