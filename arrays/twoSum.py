class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndexMap = {}

        for i in range(0, len(nums)):
            if (target - nums[i]) in numToIndexMap:
                return [numToIndexMap[target - nums[i]], i]

            if nums[i] not in numToIndexMap:
                numToIndexMap[nums[i]] = i


        return [-1, -1]
