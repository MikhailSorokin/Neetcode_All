class Solution
    # Mike - https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
    def longestSubarray(self, nums: List[int]) -> int:
        zeroCount = 0
        longestWindow = 0
        start = 0
        n = len(nums)

        for i in range(n):
            zeroCount += (nums[i] == 0)

            # Shrink until count of zeros is <= 1
            while zeroCount > 1:
                zeroCount -= (nums[start] == 0)
                start += 1

            longestWindow = max(longestWindow, i - start)

        return longestWindow