class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def isValidCell(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] != -1

        # BFS Traversal starting from the all the treasure chests in the grid
        treasures = []
        m = len(grid)
        n = len(grid[0])

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    treasures.append((row, col))

        # Start BFS
        directions = [ (1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque(treasures)
        visited = set(treasures)
        count = -1
        while queue:
            num_cells = len(queue)
            count += 1

            for _ in range(num_cells):
                row, col = queue.popleft()
                grid[row][col] = count
                for path in directions:
                    next_row, next_col = row + path[0], col + path[1]
                    if isValidCell(next_row, next_col) and (next_row, next_col) not in visited:
                        visited.add((next_row, next_col))
                        queue.append((next_row, next_col))


