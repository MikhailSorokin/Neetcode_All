class Solution:

    def isAlphaNumeric(self, char):
        return (ord('a') <= ord(char.lower()) <= ord('z') or
               ord('0') <= ord(char) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not self.isAlphaNumeric(s[right]):
                right -= 1
            while left < right and not self.isAlphaNumeric(s[left]):
                left += 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True