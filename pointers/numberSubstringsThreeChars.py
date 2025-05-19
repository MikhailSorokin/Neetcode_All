from collections import Counter

# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        counter = Counter()

        left = 0
        for right in range(n):
            counter[s[right]] += 1
            while counter['a'] > 0 and counter['b'] > 0 and counter['c'] > 0:
                counter[s[left]] -= 1
                left += 1
                res += len(s) - right

        return res
