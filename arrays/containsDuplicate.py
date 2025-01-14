class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countMap = {}
        for i in range(0, len(nums)):
            if nums[i] not in countMap:
                countMap[nums[i]] = 1
            else:
                return True

        return False         