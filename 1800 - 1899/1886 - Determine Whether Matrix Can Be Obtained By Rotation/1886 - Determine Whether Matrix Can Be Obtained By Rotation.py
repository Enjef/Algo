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

    def findRotation_v2(self, mat, target) -> bool:  # 23.07% 98.96%
        n = len(mat)
        for _ in range(4):
            if mat == target:
                return True
            mat.reverse()
            for i in range(n):
                for j in range(i):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        return False

    def findRotation_2nd_best_speed(self, mat, target) -> bool:
        for _ in range(4): 
            if mat == target: return True
            mat = [list(x)[::-1] for x in zip(*mat[:])]
        return False 

    def findRotation_3d_best_speed(self, mat, target) -> bool:
        n = len(mat)
        all_array = []
        curr_mat = mat
        for _ in range(3):
            new = []
            for j in range(n):
                curr = []
                for i in range(n - 1, -1, -1):
                    curr.append(curr_mat[i][j])
                new.append(curr)
            all_array.append(new)
            curr_mat = new
        all_array.append(mat)
        return target in all_array
