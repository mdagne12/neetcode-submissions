class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            num_set = set()
            for j in range(len(board[0])):
                if board[i][j].isdigit() and board[i][j] in num_set:
                    print("1: " + str(board[i][j]))
                    return False
                
                num_set.add(board[i][j])

        for j in range(len(board[0])):
            num_set = set()
            for i in range(len(board)):
                if board[i][j].isdigit() and board[i][j] in num_set:
                    print("2: " + str(board[i][j]))
                    return False
                
                num_set.add(board[i][j])

        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                num_set = set()

                for k in range(3):
                    for m in range(3):
                        if board[i+k][j+m].isdigit() and board[i+k][j+m] in num_set:
                            print("3: " + str(board[i + k][j + m]))
                            return False
                        
                        num_set.add(board[i + k][j + m])

        return True



        