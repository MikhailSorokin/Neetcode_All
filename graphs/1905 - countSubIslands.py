from collections import deque

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        subIslands = 0

        dirs = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        n = len(grid2)
        m = len(grid2[0])
        visited = [[False] * m for _ in range(n)]

        def bfs(row, col):
            queue = deque()
            queue.appendleft((row, col))
            visited[row][col] = True
            isSubIsland = grid1[row][col] == 1

            while queue:
                row, col = queue.popleft()
                for x, y in dirs:
                    newRow, newCol = row + y, col + x
                    if 0 <= newRow < n and 0 <= newCol < m:
                        if grid2[newRow][newCol] == 1 and not visited[newRow][newCol]:
                            visited[newRow][newCol] = True
                            queue.appendleft((newRow, newCol))
                            if grid1[newRow][newCol] == 0:
                                isSubIsland = False

            return isSubIsland

        # Go through grid2 island
        for row in range(n):
            for col in range(m):
                if grid2[row][col] == 1 and not visited[row][col]:
                    if bfs(row, col):
                        subIslands += 1

        return subIslands