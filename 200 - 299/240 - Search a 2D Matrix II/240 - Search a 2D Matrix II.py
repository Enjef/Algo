class Solution:
    def searchMatrix(
            self,
            matrix: List[List[int]], target: int) -> bool:  # 58.39% 39.79%
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] > target:
                    break
            else:
                if matrix[i][j] == target:
                    return True
            if matrix[i][j-1] == target:
                    return True
        return False

    def searchMatrix_best_speed(
            self,
            matrix: List[List[int]],
            target: int) -> bool:
        row = 0
        col = len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False

    def searchMatrix_2nd_best_speed(
            self,
            matrix: List[List[int]],
            target: int) -> bool:
        n = len(matrix[0])
        for j in range(len(matrix)):
            L, R = 0, n-1
            while L <= R:
                mid = (R-L)//2 + L
                if matrix[j][mid] == target:
                    return True
                elif matrix[j][mid] > target:
                    R = mid-1
                else:
                    L = mid+1
        return False

    def searchMatrix_best_memory(
            self,
            matrix: List[List[int]],
            target: int) -> bool:
        i, j = len(matrix) - 1, 0
        while (i >= 0 and i < len(matrix) and j >=0 and j < len(matrix[0])):
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                i -= 1
            if matrix[i][j] < target:
                j += 1              
        return False
