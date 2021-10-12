class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        out = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 1:
                    temp = [line[col] for line in mat]
                    col_count = temp.count(1)
                    row_count = mat[row].count(1)
                    if col_count + row_count == 2:
                        out += 1
        return out
