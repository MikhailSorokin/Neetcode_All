class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagramMap = defaultdict(int)
        for char in s:
            anagramMap[char] += 1

        for char in t:
            anagramMap[char] -= 1

        for k, v in anagramMap.items():
            if v != 0:
                return False

        return True
     