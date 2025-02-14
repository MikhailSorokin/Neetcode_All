class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def dfs(i, j):
            if j == n:
                return i == m
            
            match = i < m and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < n and p[j + 1] == "*":
                return (dfs(i, j + 2) or          # don't use * 
                       (match and dfs(i + 1, j))) # use *
            if match:
                return dfs(i + 1, j + 1)
            return False
        
        return dfs(0, 0)