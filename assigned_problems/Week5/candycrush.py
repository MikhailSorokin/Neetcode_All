class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m = len(board)
        n = len(board[0])

        needCrush = False

        # check horizontally
        for i in range(m):
            for j in range(n - 2):
                if abs(board[i][j]) == abs(board[i][j + 1]) == abs(board[i][j + 2]) != 0:
                    board[i][j] = board[i][j + 1] = board[i][j + 2] = -abs(board[i][j])
                    needCrush = True

        # check vertically
        for i in range(m - 2):
            for j in range(n):
                if abs(board[i][j]) == abs(board[i + 1][j]) == abs(board[i + 2][j]) != 0:
                    board[i][j] = board[i + 1][j] = board[i + 2][j] = -abs(board[i][j])
                    needCrush = True

        # crush
        for j in range(n):
            anker_i = m - 1

            for i in range(m - 1, -1, -1):
                if board[i][j] > 0:
                    board[anker_i][j] = board[i][j]
                    anker_i -= 1

            for i in range(anker_i + 1):
                board[i][j] = 0

        return self.candyCrush(board) if needCrush else board
