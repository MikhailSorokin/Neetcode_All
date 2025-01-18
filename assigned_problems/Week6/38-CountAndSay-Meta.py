class Solution:
    # Mike - Meta
    # https://leetcode.com/problems/count-and-say/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
    
    # Recursive
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        s = self.countAndSay(n - 1)
        result = []
        count = 1

        #"21"
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                result.append(str(count) + s[i - 1])
                count = 1
        #"1211"
        result.append(str(count) + s[-1])
        return "".join(result)
        
    # Iterative
    def countAndSay(self, n: int) -> str:
        s = "1"
        for i in range(2, n + 1):
            result = []
            count = 1
            # n = 3, "11". i = 1 -> count = 2
            # n= 4, "21". i = 1 -> result = ["12"]. i = 2 -> exit loop. ["12", "11"] -> "1211"
            for j in range(1, len(s)):
                if s[j] == s[j - 1]:
                    count += 1
                else:
                    result.append(str(count) + s[j - 1])
                    count = 1
            result.append(str(count) + s[-1])
            s = "".join(result)
        return s