class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = set()

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        connectedComps = 0
        def dfs(node):
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        res = 0
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                connectedComps += 1

        return connectedComps
