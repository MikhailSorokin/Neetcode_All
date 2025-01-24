class Solution:
    # Mike - Meta #https://leetcode.com/problems/search-in-rotated-sorted-array/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            # Prevents potential memory overflow
            mid = left + (right - left) // 2
            # Check which one has a valid range and if we fall in it
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                # Now, check if we fall in that range
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        if nums[left] == target:
            return left
        return -1
        