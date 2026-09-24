class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        def isValidCell(row, col):
            return 0 <= row < n and 0 <= col < n

        minHeap = [ [grid[0][0], 0, 0] ]
        visited_cells = { (0, 0) }
        directions = [ (1, 0), (-1, 0), (0, -1), (0, 1) ]
        n = len(grid)

        while minHeap:
            time, row, col = heapq.heappop(minHeap)

            if row == n - 1 and col == n - 1:
                return time

            # Check whether we should add the neighbors to the heap
            for r_dir, c_dir in directions:
                new_row, new_col = row + r_dir, col + c_dir

                # Check if the neighbor is a valid cell on the grid and that we haven't already visited it
                if isValidCell(new_row, new_col) and (new_row, new_col) not in visited_cells:
                    heapq.heappush(minHeap, [max(time, grid[new_row][new_col]), new_row, new_col])
                    visited_cells.add((new_row, new_col))

        return -1