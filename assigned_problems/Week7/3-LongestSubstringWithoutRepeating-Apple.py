class Solution:
    # Saman - https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=company&envId=apple&favoriteSlug=apple-three-months
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_length = 0
        char_set = set()
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length