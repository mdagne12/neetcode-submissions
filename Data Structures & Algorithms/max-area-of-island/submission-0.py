class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def isValidLand(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1

        def dfs(row, col):
            count = 1
            for path in directions:
                next_row, next_col = row + path[0], col + path[1]
                if isValidLand(next_row, next_col) and (next_row, next_col) not in visited:
                    visited.add((next_row, next_col))
                    count += dfs(next_row, next_col)

            return count
            


        m = len(grid)
        n = len(grid[0])
        visited = set()
        directions = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]
        max_area = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row, col) not in visited:
                    visited.add((row, col))
                    max_area = max(max_area, dfs(row, col))

        return max_area
        