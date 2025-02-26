from collections import deque, defaultdict

# BFS Approach
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        for i in range(0, n):
            queue = deque([(i, None)])
            visited = set()

            while queue:
                node, parent = queue.popleft()
                for child in graph[node]:
                    if child != parent:
                        if child in visited:
                            return False
                        visited.add(child)
                        queue.append((child, node))
        
        return True
        
# DFS Approach

from collections import deque, defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        graph = defaultdict(list)

        for x, y in edges:
            #print(f'{x},{y},{graph}')
            graph[x].append(y)
            graph[y].append(x)
        
        visited = set()
        def dfs(x, parent):
            visited.add(x)
            if graph[x]:
                for child in graph[x]:
                    if child not in visited:
                        if dfs(child, x):
                            return True
                    elif child != parent:
                        return True
            return False
        
        for x in graph:
            if x not in visited:
                if dfs(x, None):
                    return False
        print(visited)
        return True
        