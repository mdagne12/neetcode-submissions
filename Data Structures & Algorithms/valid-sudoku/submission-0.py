class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        square_set = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):

                if board[i][j] == ".":
                    continue;

                num = int(board[i][j])
                square_index = math.ceil((j + 1) / 3) + math.floor(i / 3) * 3
                
                if num > 9 or num < 0:
                    return False;
                elif num in row_set[i] or num in col_set[j] or num in square_set[square_index]:
                    return False

                row_set[i].add(num)
                col_set[j].add(num)
                square_set[square_index].add(num)

        return True

                

        