class Solution:
    def findRotation(self, mat, target):  # 20.65% 88.47%
        def rotate():
            mat.reverse()
            for i in range(n):
                for j in range(i):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
        n = len(mat)
        for _ in range(4):
            rotate()
            if mat == target:
                return True
        return False
