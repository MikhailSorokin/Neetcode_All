class Solution:
    # Daniel - https://leetcode.com/problems/count-special-subsequences/?envType=company&envId=google&favoriteSlug=google-thirty-days
    def numberOfSubsequences(self, A: List[int]) -> int:
        n = len(A)
        cnt = Counter()
        res = 0
        for r in range(4, n - 2):
            q = r - 2
            for p in range(q - 1):
                cnt[A[p] / A[q]] += 1
            for s in range(r + 2, n):
                res += cnt[A[s] / A[r]]
        return res                
