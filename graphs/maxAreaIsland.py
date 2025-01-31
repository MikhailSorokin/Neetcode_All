class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])

        maxArea = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    area = 1
                    maxArea = max(maxArea, area)
                    queue = deque([(i, j)])
                    while queue:
                        row, col = queue.popleft()
                        grid[row][col] = -1

                        # Up, right, down, left
                        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
                        for dir in dirs:
                            hoz = dir[0]
                            vert = dir[1]
                            if (0 <= col + hoz < m and 0 <= row + vert < n):
                                if grid[row + vert][col + hoz] == 1:
                                    maxArea = max(maxArea, area + 1)
                                    queue.append((row + vert, col + hoz))
                                    grid[row + vert][col + hoz] = -1
                                    area += 1
  
        return maxArea
      