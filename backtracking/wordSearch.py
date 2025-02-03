class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        def dfs(row, col, i):
            if i == len(word):
                return True
            if row >= n or col >= m or row < 0 or col < 0:
                return False
            if word[i] != board[row][col] or board[row][col] == "#":
                return False
            
            board[row][col] = "#"
            res = False
            res = res or dfs(row + 1, col, i + 1)
            res = res or dfs(row, col + 1, i + 1)
            res = res or dfs(row - 1, col, i + 1)
            res = res or dfs(row, col - 1, i + 1)

            board[row][col] = word[i]
            return res


        for r in range(n):
            for c in range(m):
                if dfs(r, c, 0):
                    return True

        return False