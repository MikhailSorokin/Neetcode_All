from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # 1 -> [0]
        # Construct graph. See if there is no cycle and stop once we hit NUMCOURSES.
        # 1 -> [0]
        # 0 -> [1] 
        # 1 -> 0 -> 1. CYCLE  - STOP. Visited already
        graph = {i:[] for i in range(numCourses) } 
        indegree = defaultdict(int)
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque()
        for vertex in graph.keys():
            if indegree[vertex] == 0:
                q.append(vertex)

        setCourses = []
        counter = 0
        while q:
            curr = q.popleft()
            setCourses.append(curr)
            counter += 1

            for neighbor in graph[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        if counter != numCourses:
            return []

        return setCourses


