class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        directions = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]

        def isValid(row, col): 
            return 0 <= row < ROWS and 0 <= col < COLS

        def dfs(row, col):
            board[row][col] = "T"
            for r_dir, c_dir in directions:
                new_row, new_col = row + r_dir, col + c_dir
                if isValid(new_row, new_col) and board[new_row][new_col] == "O":
                    dfs(new_row, new_col)

        # Perform DFS on all the O's along the top and bottom border
        for row in range(ROWS):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][COLS - 1] == "O":
                dfs(row, COLS - 1)

        # Perform DFS on all the O's along the left and right border    
        for col in range(COLS):
            if board[0][col] == "O":
                dfs(0, col)
            if board[ROWS - 1][col] == "O":
                dfs(ROWS - 1, col)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
        