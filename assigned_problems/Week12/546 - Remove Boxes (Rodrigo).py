class Solution:
    # Capital One
    # https://leetcode.com/problems/remove-boxes/?envType=company&envId=capital-one&favoriteSlug=capital-one-all
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        # dp[i][j][k] = max score from subarray boxes[i..j] with k same-colored boxes
        # carried over matching boxes[i].
        dp = [[[-1]*(n+1) for _ in range(n)] for _ in range(n)]

        def f(i, j, k):
            #print(dp)
            if i > j:
                return 0
            if dp[i][j][k] != -1:
                return dp[i][j][k]

            # Step 1: combine consecutive boxes of the same color as boxes[i].
            color = boxes[i]
            i2 = i
            cnt = 0
            while i2 <= j and boxes[i2] == color:
                i2 += 1
                cnt += 1

            # Now we have cnt boxes of 'color' in [i..i2-1].
            # Option A: remove these cnt boxes (plus k carried) and solve remainder
            res = (k + cnt) * (k + cnt) + f(i2, j, 0)

            # Option B: try to merge them with a same-colored box further right
            for m in range(i2, j+1):
                if boxes[m] == color:
                    # remove subarray [i2..m-1], then combine color with (k+cnt)
                    res = max(res, f(i2, m-1, 0) + f(m, j, k + cnt))

            dp[i][j][k] = res
            return res

        res = f(0, n-1, 0)
        #print(dp)
        return res
