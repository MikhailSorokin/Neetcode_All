from collections import deque

# https://leetcode.com/problems/making-a-large-island/description/
class Solution:

    def innerBFS(self, startRow, startCol, grid, islandId):
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        queue = deque([(startRow, startCol)])
        currSize = 1
        grid[startRow][startCol] = islandId

        while queue:
            row, col = queue.popleft()

            for x, y in dirs:
                newRow = row + y
                newCol = col + x

                if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[newRow]):
                    if grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = islandId
                        currSize += 1
                        queue.append((newRow, newCol))

        return currSize

    def largestIsland(self, grid: List[List[int]]) -> int:

        # Store the maximum area
        maxIslandSize = 0
        islandId = 2
        islandMap = {}

        # Get a list of all the 0s and then BFS from there where
        queue = deque()
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        n = len(grid)
        for row in range(n):
            m = len(grid[row])
            for col in range(m):
                if grid[row][col] == 1:
                    islandSize = self.innerBFS(row, col, grid, islandId)
                    islandMap[islandId] = islandSize
                    islandId += 1

        maxIsland = max(islandMap.values(), default=0)

        # We still need to BFS through and see if we have seen islandID
        for row in range(n):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    seen = set()
                    currIslandSize = 1
                    for x, y in dirs:
                        newRow, newCol = row + y, col + x
                        if 0 <= newRow < n and 0 <= newCol < len(grid[newRow]) and grid[newRow][newCol] > 1:
                            cachedId = grid[newRow][newCol]
                            if cachedId not in seen:
                                seen.add(cachedId)
                                currIslandSize += islandMap[cachedId]
                            
                    maxIslandSize = max(maxIslandSize, currIslandSize)

        return maxIslandSize if maxIslandSize != 0 else n * n