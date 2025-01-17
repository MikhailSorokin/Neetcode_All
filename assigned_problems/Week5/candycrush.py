class Solution:
    # daniel's solution
    # https://leetcode.com/problems/candy-crush/submissions/1511435350/
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m = len(board) # num rows
        n = len(board[0]) # num columns
        needCrush = False # boolean check

        # check horizontally
        for i in range(m): # iterate rows
            for j in range(n - 2): # iterate columns
                if abs(board[i][j]) == abs(board[i][j + 1]) == abs(board[i][j + 2]) != 0:
                    board[i][j] = board[i][j + 1] = board[i][j + 2] = -abs(board[i][j])
                    needCrush = True

        # check vertically
        for j in range(n): # iterate colums
            for i in range(m - 2): # iterate rows
                if abs(board[i][j]) == abs(board[i + 1][j]) == abs(board[i + 2][j]) != 0:
                    board[i][j] = board[i + 1][j] = board[i + 2][j] = -abs(board[i][j])
                    needCrush = True

        # crush
        for j in range(n): # iterate through columns
            anker_i = m - 1 # the row where the above value drops to

            for i in range(m - 1, -1, -1): # iterate rows
                # crushed candies are marked as negative
                # drop non crushed candies to anchor
                if board[i][j] > 0: 
                    board[anker_i][j] = board[i][j]
                    anker_i -= 1

            # clear above spaces to zero
            for i in range(anker_i + 1):
                board[i][j] = 0

        return self.candyCrush(board) if needCrush else board
