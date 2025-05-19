from collections import deque, defaultdict

# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        paths = deque()
        minDist = float('inf')
        adjGraph = defaultdict(list)

        # Find where we can start at road 1
        for road in roads:
            roadA, roadB, cost = road 
            adjGraph[roadA].append([roadB, cost])
            adjGraph[roadB].append([roadA, cost])

        vis = [False] * (n + 1)
        paths.appendleft(1)
        vis[1] = True

        while paths:
            node = paths.popleft()

            # Add neighbors to queue UNLESS roadA is at n
            for neighbor, cost in adjGraph[node]:
                minDist = min(minDist, cost)
                if vis[neighbor] == False:
                    vis[neighbor] = True
                    paths.appendleft(neighbor)
        
        return minDist
