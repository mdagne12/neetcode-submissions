class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Returns true if the location exists on the grid and represents land
        def isValidLand(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == "1":
                return True

        def dfs(row, col):
            for row_dir, col_dir in directions:
                new_row, new_col = row + row_dir, col + col_dir
                if isValidLand(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    dfs(new_row, new_col)

        directions = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]
        seen = set()
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in seen:
                    ans += 1
                    seen.add((i, j))
                    dfs(i, j)

        return ans
