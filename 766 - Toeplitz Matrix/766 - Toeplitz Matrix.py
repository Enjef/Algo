class Solution:
    def isToeplitzMatrix(
            self,
            matrix: List[List[int]]) -> bool:  # 91.58% 7.20%
        dia_map = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                cur = i-j
                if cur not in dia_map:
                    dia_map[cur] = matrix[i][j]
                if dia_map[cur] != matrix[i][j]:
                    return False
        return True

    def isToeplitzMatrix_best_speed(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)-1):
            top_line = matrix[i]
            next = top_line[:-1]
            test = matrix[i+1][1::]
            if test != next:
                return False
        return True

    def isToeplitzMatrix_best_memory(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        for r in range(row-1):
            for c in range(col-1):
                if matrix[r][c] != matrix[r+1][c+1]:
                    return False
        return True
