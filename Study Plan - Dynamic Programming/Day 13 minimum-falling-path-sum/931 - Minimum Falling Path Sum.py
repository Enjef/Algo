class Solution:
    def minFallingPathSum(
            self,
            matrix: List[List[int]]) -> int:  # 21.11% 58.43%
        n = len(matrix)
        
        for i in range(1, n):
            matrix[i][0] += min(matrix[i-1][0], matrix[i-1][1])
            for j in range(1, len(matrix[i])-1):
                matrix[i][j] += (
                    min(
                        matrix[i-1][j-1],
                        matrix[i-1][j],
                        matrix[i-1][j+1]
                    ))
            matrix[i][-1] += min(matrix[i-1][-1], matrix[i-1][-2])
        return min(matrix[-1])
