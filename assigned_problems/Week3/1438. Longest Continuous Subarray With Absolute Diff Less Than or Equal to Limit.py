class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0  # Left pointer of the sliding window
        max_length = 0

        # Use a sliding window
        for right in range(len(nums)):
            # Calculate the current subarray's max and min
            current_max = max(nums[left:right+1])
            current_min = min(nums[left:right+1])

            # Check if the window is valid
            if current_max - current_min > limit:
                # Shrink the window by moving the left pointer
                left += 1

            # Update the maximum length of the valid window
            max_length = max(max_length, right - left + 1)

        return max_length
