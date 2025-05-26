from collections import deque
from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Add all land cells to the queue
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))

        # If all are land or all are water, return -1
        if len(queue) == 0 or len(queue) == n * n:
            return -1

        distance = -1
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in dirs:
                    r, c = row + dr, col + dc
                    if 0 <= r < n and 0 <= c < n and grid[r][c] == 0:
                        grid[r][c] = 1  # Mark as visited
                        queue.append((r, c))
            distance += 1

        return distance