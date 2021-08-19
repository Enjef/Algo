class Solution:
    def transpose(
            self,
            matrix: List[List[int]]) -> List[List[int]]:  # 64.46% 99.81%
        return list(zip(*matrix))

    def transpose_best_speed(self, matrix: List[List[int]]) -> List[List[int]]:
        t = []
        for j in range(len(matrix[0])):
            t.append([])
            for i in range(len(matrix)):
                t[j].append(matrix[i][j])
        return t

    def transpose_best_memory(
            self,
            matrix:
            List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(matrix[0])):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            res.append(temp)
        return res
