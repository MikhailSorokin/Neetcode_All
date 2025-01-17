class Solution:

    def isAlphaNumeric(self, char):
        return (0 <= ord(char.lower()) - ord('a') <= 26 or
               0 <= ord(char) - ord('0') <= 9)

    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0
        right = len(s) - 1
        while left <= right:
            while left < right and not self.isAlphaNumeric(s[right]):
                right -= 1
            while left < right and not self.isAlphaNumeric(s[left]):
                left += 1

            if left >= right:
                return True

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True