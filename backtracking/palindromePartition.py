class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(sCopy, left, right):
            while left < right:
                if sCopy[left] != sCopy[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(i, sList):
            # Base case. i == n
            if i == len(s):
                res.append(sList.copy())
                return

            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    sList.append(s[i : j + 1])
                    dfs(j + 1, sList)
                    sList.pop()

        dfs(0, [])
        return res