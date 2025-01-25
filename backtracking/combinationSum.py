class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        combinationSumLst = []
 
        def dfs(i, curr, total):
            if total == target:
                combinationSumLst.append(curr.copy())
                return 
            # BASE CASE
            # When we reach the end
            if i >= len(nums) or total > target:
                return

            # Add the current nums
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return combinationSumLst