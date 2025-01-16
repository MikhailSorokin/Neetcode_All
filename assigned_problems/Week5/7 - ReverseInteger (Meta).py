class Solution:
    # Mike 
    # https://leetcode.com/problems/reverse-integer/
    def reverse(self, x: int) -> int:
            queue = []
            mul = -1 if x < 0 else 1
            x = -x if x < 0 else x

            while x != 0:
                queue.append(x % 10)
                x = x // 10

            res = 0
            while queue:
                n = len(queue)
                front = queue.pop(0)
                res += pow(10, n - 1) * front

            # NOTE: This problem requires us to have <= 2^31 - 1
            if res > pow(2, 31) - 1:
                return 0

            return res * mul
        