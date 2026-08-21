class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Returns true if the location is a valid spot on the grid and represents land
        def isValidLand(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1:
                return True

        def dfs(row, col):
            ans = 1
            for r_dir, c_dir in directions:
                new_row, new_col = row + r_dir, col + c_dir
                if isValidLand(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    ans += dfs(new_row, new_col)
            return ans


        directions = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]
        max_area = 0
        seen = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in seen:
                    seen.add((i, j))
                    max_area = max(max_area, dfs(i, j))

        return max_area