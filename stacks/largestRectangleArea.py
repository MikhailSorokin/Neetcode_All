class Solution:
    # Monotonic stack method
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] 
        heights.append(0) # dummy node in the tail
        max_area = 0
        for i, cur_height in enumerate(heights):
            while stack and heights[stack[-1]] > cur_height:
                height = heights[stack.pop()]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                max_area = max(max_area, width * height)
            stack.append(i)
        return max_area
        