
    # Daniel - Google
    #https://leetcode.com/problems/first-missing-positive/?envType=company&envId=google&favoriteSlug=google-thirty-days
# brute force
# sort the array
# start iterating, if 1 is present, then increment,
# if 2 is present, increment,
# wherever the increment stops is the smallest positive integer

# O(n) time, O(n) - suboptimal
# use a separate hashset to track the smallest positive integer
'''
from typing import List

def firstMissingPositiveHashSet(nums: List[int]) -> int:
    num_set = set(nums)  # Store all numbers in a hash set
    
    for i in range(1, len(nums) + 2):  # Check from 1 to n+1
        if i not in num_set:
            return i  # Return the first missing positive
'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
    
        # Step 1: Replace negative numbers and zeros with n+1
        for i in range(n):
            # if number is negative or greater than n
            if nums[i] <= 0 or nums[i] > n:
                # replace with placeholder value, n + 1
                nums[i] = n + 1
        
        # Step 2: Mark existing numbers by negating them
        for i in range(n):
            # take absolute value 
            # because it might have already marked as negative
            # if previously encountered
            val = abs(nums[i])
            if 1 <= val <= n:
                nums[val - 1] = -abs(nums[val - 1])
        
        # Step 3: Find the first missing positive
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        return n + 1      

# Example 2
# [3,4,5,1] Step 1
# [-3,4,-5,-1] Step 2
# Step 3
# i = 0 -> present
# i = 1 -> missing, return 2
     
