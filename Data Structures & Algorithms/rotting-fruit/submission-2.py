class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def isValidFruit(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1
        
        rotten = []
        m, n = len(grid), len(grid[0])
        fruit_count = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    rotten.append((row, col))
                if grid[row][col] == 1 or grid[row][col] == 2:
                    fruit_count += 1

        queue = deque(rotten)
        visited = set(rotten)
        directions = [ (-1, 0), (1, 0), (0, -1), (0, 1)]
        count = -1
        while queue:
            num_fruits = len(queue)
            count += 1

            for _ in range(num_fruits):
                row, col = queue.popleft()

                for path in directions:
                    next_row, next_col = row + path[0], col + path[1]
                    if isValidFruit(next_row, next_col) and (next_row, next_col) not in visited:
                        visited.add((next_row, next_col))
                        queue.append((next_row, next_col))
                        
        if count == -1:
            count = 0

        return count if len(visited) == fruit_count else -1

