from collections import deque, defaultdict

class Solution:
    # https://leetcode.com/problems/find-champion-ii/description/
    # Problem 2924

    # INCORRECT VERSION - BUT CLOSE 
    '''def findChampion(self, n: int, edges: List[List[int]]) -> int:
        adjGraph = defaultdict(list)
        for u, v in edges:
            adjGraph[u].append(v)

        memo = {}
        lastChecked = -1
        # BFS through all nodes and track visited
        for i in range(n):
            visited = set()

            queue = deque()
            queue.append(i)
            visited.add(i)

            while queue:
                if len(visited) == n:
                    return i

                node = queue.popleft()
                if node in memo:
                    visited.add(memo[node])
                    if len(visited) == n:
                        return i
                    continue
                for neighbor in adjGraph[node]:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    memo[node] = neighbor

        return -1 
    '''

    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        # Initialize the indegree array to track the number of incoming edges for each team
        indegree = [0] * n

        # Store the indegree of each team
        for edge in edges:
            indegree[edge[1]] += 1

        champ = -1
        champ_count = 0

        # Iterate through all teams to find those with an indegree of 0
        for i in range(n):
            # If the team can be a champion, store the team number and increment the count
            if indegree[i] == 0:
                champ_count += 1
                champ = i

        # If more than one team can be a champion, return -1, otherwise return the champion team number
        return champ if champ_count == 1 else -1

