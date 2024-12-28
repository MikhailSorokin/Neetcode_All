class Solution:
    def findHelper(self, target, nums):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return True
        
        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Search through each row to see if target is between 1 and last
        rows = len(matrix)

        found = False
        for i in range(0, rows):
            colArray = matrix[i]
            found = self.findHelper(target, colArray)
            if found:
                return True

        return found
