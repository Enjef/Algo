class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:  # 96.64% 59.65%
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return

    def rotate_mock(self, matrix: List[List[int]]) -> None:  # 69.19% 85.72%
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = matrix[::-1]
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

    def rotate_best_speed(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 1:
            return matrix
        for it in range(n//2):
            for i in range(it, n-1-it):

                temp = matrix[it][i]
                matrix[it][i] = matrix[n-1-i][it]
                matrix[n-1-i][it] = matrix[n-1-it][n-1-i]
                matrix[n-1-it][n-1-i] = matrix[i][n-1-it]
                matrix[i][n-1-it] = temp
        return matrix

    def rotate_2nd_best_speed(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        start, end = 0, n - 1
        while start < end:
            matrix[start], matrix[end] = matrix[end], matrix[start]
            start += 1
            end -= 1
        for row_idx, row in enumerate(list(zip(*matrix))):
            matrix[row_idx] = row

    def rotate_best_memory(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        cen = (n-1)/2
        if n % 2 == 0:
            i_max = int(n/2)
            j_max = int(n/2)
        else:
            i_max = int(n/2) + 1
            j_max = int(n/2)
        for i in range(i_max):
            for j in range(j_max):
                r = i - cen
                c = j - cen
                temp1 = matrix[i][j]
                for k in range(4):
                    r_n = c
                    c_n = - r
                    temp2 = matrix[int(r_n + cen)][int(c_n + cen)]
                    matrix[int(r_n + cen)][int(c_n + cen)] = temp1
                    r = r_n
                    c = c_n
                    temp1 = temp2

    def rotate_2nd_best_memory(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1. row swap 
        length = len(matrix)
        row_mid = int(length/2)-1 if length%2==0 else length//2 - 1
        for i in range(row_mid + 1):
            op_i = length - i - 1
            temp = matrix[op_i]
            matrix[op_i] = matrix[i]
            matrix[i] = temp
        # 2. tanspose
        for i in range(length):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
