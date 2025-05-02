class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans, left = 0, 0
        frequency = defaultdict(int)
        for right in range(len(nums)):
            frequency[nums[right]] += 1
            while frequency[nums[right]] > k:
                frequency[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans