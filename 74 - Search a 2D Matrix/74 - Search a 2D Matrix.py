class Solution:
    def searchMatrix(
            self,
            matrix: List[List[int]],
            target: int) -> bool:  # 13.21% 33.67%
        left = 0
        right = len(matrix) * len(matrix[0])
        while left <= right:
            mid = left + (right - left) // 2
            row_mid, col_mid = divmod(mid, len(matrix[0]))
            if (
                    len(matrix)-1 < row_mid or row_mid < 0 or
                    len(matrix[0])-1 < col_mid or col_mid < 0):
                return False
            if matrix[row_mid][col_mid] == target:
                return True
            if matrix[row_mid][col_mid] > target:
                right = mid - 1
            if matrix[row_mid][col_mid] < target:
                left = mid + 1
        return False

    def searchMatrix_refactored(
            self,
            matrix: List[List[int]],
            target: int) -> bool:  # 64.28% 33.67%
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            row_mid, col_mid = divmod(mid, len(matrix[0]))
            if matrix[row_mid][col_mid] == target:
                return True
            if matrix[row_mid][col_mid] > target:
                right = mid - 1
            if matrix[row_mid][col_mid] < target:
                left = mid + 1
        return False

    def searchMatrix_in_row(
            self,
            matrix: List[List[int]],
            target: int) -> bool:  # 19.26% 63.51%
        for row in matrix:
            if target in row:
                return True
        return False

    def searchMatrix_best_speed(
            self,
            matrix: List[List[int]],
            target: int) -> bool:
        if not matrix or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n-1
        while left <= right:
            mid = (left + right)//2
            r, c = mid // n, mid % n
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
