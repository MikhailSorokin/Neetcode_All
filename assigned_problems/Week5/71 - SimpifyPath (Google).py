class Solution:
    # Daniel - Google 
    # https://leetcode.com/problems/maximum-swap/?envType=company&envId=google&favoriteSlug=google-three-months
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))

        max_digit = "0"
        max_i = -1
        swap_i = swap_j = -1
        for i in reversed(range(len(nums))):
            # track max
            if nums[i] > max_digit:
                max_digit = nums[i]
                max_i = i
            # track swap
            if nums[i] < max_digit:
                swap_i, swap_j = i, max_i

        nums[swap_i], nums[swap_j] = nums[swap_j], nums[swap_i]

        return int("".join(nums))
