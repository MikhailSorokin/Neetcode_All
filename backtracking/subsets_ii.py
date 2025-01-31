class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()

        def dfs(idx, lst):
            if idx == n:
                res.add(tuple(lst))
                return
            
            res.add(tuple(lst))
            lst.append(nums[idx])
            dfs(idx + 1, lst)
            lst.pop()
            dfs(idx + 1, lst)

        nums.sort()
        dfs(0, [])
        return [list(tup) for tup in res]