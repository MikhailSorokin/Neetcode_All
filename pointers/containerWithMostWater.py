class Solution:
    #75% runtime passing
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        left, right = 0, n - 1
        while left < right:
            maxArea = max(maxArea, min(heights[left], heights[right]) * (right - left))

            if heights[left] < heights[right]:
                left += 1
            elif heights[left] == heights[right]:
                left += 1
                right -= 1
            else:
                right -= 1


        return maxArea