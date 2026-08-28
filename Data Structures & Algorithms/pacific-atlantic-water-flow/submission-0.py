class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]

        def isValid(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS

        def dfs(row, col, ocean_set):
            for r_dir, c_dir in directions:
                new_row, new_col = row + r_dir, col + c_dir
                if isValid(new_row, new_col) and heights[row][col] <= heights[new_row][new_col] and (new_row, new_col) not in ocean_set:
                    ocean_set.add((new_row, new_col))
                    dfs(new_row, new_col, ocean_set)

        pacific = set()
        atlantic = set()

        for row in range(ROWS):
            pacific.add((row, 0))
            dfs(row, 0, pacific)
            atlantic.add((row, COLS - 1))
            dfs(row, COLS - 1, atlantic)

        for col in range(COLS):
            pacific.add((0, col))
            dfs(0, col, pacific)
            atlantic.add((ROWS - 1, col))
            dfs(ROWS - 1, col, atlantic)

        result = []
        for cell in pacific:
            if cell in atlantic:
                result.append(cell)

        return result




        