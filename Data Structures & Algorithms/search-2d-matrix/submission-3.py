class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) * len(matrix[0]) - 1
        # left = 0, right = 1
        while left <= right:
            middle = (left + right) // 2    # 0

            mid_row = middle // len(matrix[0])  # 0
            mid_col = middle % len(matrix[0])   # 0

            if target == matrix[mid_row][mid_col]:
                return True
            elif target < matrix[mid_row][mid_col]:
                right = middle - 1
            else:
                left = middle + 1

        return False
