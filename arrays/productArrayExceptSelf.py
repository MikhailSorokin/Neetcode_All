class Solution:

    # Brute force:
    # [1, 2, 4, 6]. Multiply sum of products to get 48

    # Another pass to store at index and divde by that #
    # [48, 24, 12, 8]

    # Optimal solution:
    # New array
    # [1, 1, 1, 1]
    # [1, 1, 1, 1]

    # [1, 1, 2, 8]
    # [48, 24, 6, 1]

    # [48, 24, 12, 8]


    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefixes
        n = len(nums)
        prefixes = [1] * n
        suffixes = [1] * n

        # Prefix starts at 1
        curr = 1
        for i in range(0, n):
            prefixes[i] = curr
            curr *= nums[i]
        
        # Suffix goes from end
        curr = 1
        for i in range(n - 1, -1, -1):
            suffixes[i] = curr
            curr *= nums[i]

        # Multiply
        for i in range(0, n):
            nums[i] = prefixes[i] * suffixes[i]

        return nums

        