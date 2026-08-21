from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def isValidLand(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == INF

        INF = 2147483647
        queue = deque()

        # add all the treasure 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))

        directions = [ (0, 1), (0, -1), (1, 0), (-1, 0)]
        distance = 1

        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()

                for r_dir, c_dir in directions:
                    new_row, new_col = row + r_dir, col + c_dir
                    if isValidLand(new_row, new_col):
                        grid[new_row][new_col] = distance
                        queue.append((new_row, new_col))

            distance += 1

        