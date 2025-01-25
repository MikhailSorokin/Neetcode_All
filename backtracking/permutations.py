class Solution:
    # Beats 100% of permutation
    def permute(self, nums: List[int]) -> List[List[int]]:
        accum = []
        n = len(nums)
        
        def dfs(i, seen):
            seen.append(nums[i])

            if len(seen) == n:
                accum.append(seen)
                return

            for j in range(0, n):
                if nums[j] not in seen:
                    dfs(j, seen.copy())

        for i in range(0, n):
            dfs(i, [])
        return accum