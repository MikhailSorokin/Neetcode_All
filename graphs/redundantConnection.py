class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        def dfs(node, parent):
            # Base case
            if node in visited:
                return True

            visited.add(node)

            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if dfs(neighbor, node):
                    return True


            return False

        res = 0
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = set()

            if dfs(u, None):
                return [u, v]

        return []
