class Solution:
    # Daniel - Google
    #https://leetcode.com/problems/first-missing-positive/?envType=company&envId=google&favoriteSlug=google-thirty-days
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
    
        # Step 1: Replace negative numbers and zeros with n+1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        
        # Step 2: Mark existing numbers
        for i in range(n):
            val = abs(nums[i])
            if 1 <= val <= n:
                nums[val - 1] = -abs(nums[val - 1])
        
        # Step 3: Find the first missing positive
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        return n + 1        
