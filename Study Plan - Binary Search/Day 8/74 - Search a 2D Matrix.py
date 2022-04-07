class Solution:
    def searchMatrix(self, matrix, target) -> bool:  #84.15% 46.78%
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n-1
        while left <= right:
            mid = left + (right-left)//2
            row, col = divmod(mid, n)
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                right = mid - 1            
            else:
                left = mid + 1
        return False
