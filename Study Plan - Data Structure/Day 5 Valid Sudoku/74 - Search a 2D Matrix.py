class Solution:
    def searchMatrix(
            self,
            matrix: List[List[int]],
            target: int) -> bool:
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
