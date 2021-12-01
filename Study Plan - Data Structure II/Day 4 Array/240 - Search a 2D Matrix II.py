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

    def searchMatrix_v2(
            self,
            matrix: List[List[int]], target: int) -> bool:  # 46.18% 74.69%
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] > target:
                    if matrix[i][j-1] == target:
                        return True
                    break
            if matrix[i][j] == target:
                return True
        return False
