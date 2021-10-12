class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonals = {}   # 74.12% 52.96%
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i - j not in diagonals:
                    diagonals[i-j] = []
                diagonals[i-j].append(mat[i][j])
        for val in diagonals.values():
            val.sort()
        for i in range(len(mat)-1, -1, -1):
            for j in range(len(mat[0])-1, -1, -1):
                mat[i][j] = diagonals[i-j].pop()
        return mat

    def diagonalSort_pop(self, mat: List[List[int]]) -> List[List[int]]:
        diagonals = {}   # 96.83% 78.66%
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i - j not in diagonals:
                    diagonals[i-j] = []
                diagonals[i-j].append(mat[i][j])
        for val in diagonals.values():
            val.sort()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = diagonals[i-j].pop(0)
        return mat
