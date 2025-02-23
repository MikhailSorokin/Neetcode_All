from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1 -> [0]
        # Construct graph. See if there is no cycle and stop once we hit NUMCOURSES.
        # 1 -> [0]
        # 0 -> [1] 
        # 1 -> 0 -> 1. CYCLE  - STOP. Visited already
        if len(prerequisites) == 0:
            return True

        graph = {i:[] for i in range(numCourses) }
        inward_connections = defaultdict(int)

        for a, b in prerequisites:
            graph[b].append(a)
            inward_connections[a] += 1

        q = deque()
        for vertex in graph.keys():
            if inward_connections[vertex] == 0:
                q.append(vertex)

        counter = 0
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                counter += 1
                print(f'{curr},{counter}')
                for vertex in graph[curr]:
                    inward_connections[vertex] -= 1
                    if inward_connections[vertex] == 0: 
                        q.append(vertex)

        return counter == numCourses

