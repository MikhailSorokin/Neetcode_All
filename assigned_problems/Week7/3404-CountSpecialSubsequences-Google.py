class Solution:
    # Daniel - https://leetcode.com/problems/count-special-subsequences/?envType=company&envId=google&favoriteSlug=google-thirty-days
    def numberOfSubsequences(self, A: List[int]) -> int:
        n = len(A)
        count = Counter()
        res = 0
        for r in range(4, n - 2): # let r take the lead
            q = r - 2
            for p in range(q - 1):
                count[A[p] / A[q]] += 1
            for s in range(r + 2, n):
                res += count[A[s] / A[r]]
        return res        

        #0  1  2  3
        # [a, b, c, d, e]
        #0     2  |  4   6
        # nums[p] * nums[r] == nums[q] * nums[s]
        # nums[p]/nums[q] == nums[s]/nums[r]

        # for r in range(4, n-2)
        #     # for q in range(2, r-2)
        #     q = r - 2
        #     for p in range(0, q-2)

        #     for s in range(r + 2, n)

        # for r in range(4, n-2)
        #     for q in range()              
