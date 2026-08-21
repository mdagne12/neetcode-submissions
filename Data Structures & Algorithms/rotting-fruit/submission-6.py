from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def isFreshOrange(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1

        # Count the number of fresh fruit and add all the 
        # original rotten oranges to the queue for BFS later
        fresh_count = 0
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        directions = [ (0, 1), (0, -1), (1, 0), (-1, 0)]
        seen = set()
        time = 0

        while fresh_count > 0 and queue:

            for i in range(len(queue)):
                row, col = queue.popleft()
                for r_dir, c_dir in directions:
                    new_row, new_col = row + r_dir, col + c_dir
                    if isFreshOrange(new_row, new_col) and (new_row, new_col) not in seen:
                        seen.add((new_row, new_col))
                        queue.append((new_row, new_col))
                        fresh_count -= 1

            time += 1

        return time if fresh_count == 0 else -1
        