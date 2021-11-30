class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:  # 74.52% 19.50%
        up_border = left_border = 0
        down_border = right_border = n - 1
        mat = [[0]*n for _ in range(n)]
        mat[0][0] = 1
        i = j = 0
        cur = 1
        while cur < n * n:
            if i == up_border and j == left_border:
                if not(i == 0 and j == 0):
                    left_border += 1
                while j < right_border:
                    j += 1
                    cur += 1
                    mat[i][j] = cur
            elif i == up_border and j == right_border:
                up_border += 1
                while i < down_border:
                    i += 1
                    cur += 1
                    mat[i][j] = cur
            elif i == down_border and j == right_border:
                right_border -= 1
                while j > left_border:
                    j -= 1
                    cur += 1
                    mat[i][j] = cur
            elif i == down_border and j == left_border:
                down_border -= 1
                while i > up_border:
                    i -= 1
                    cur += 1
                    mat[i][j] = cur
        return mat
        
    def generateMatrix_best_speed(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for j in range(n)]
        x, y = 0, 0
        maxX, maxY = n-1, n-1
        val = 1
        direction = 0
        while x <= maxX and y <= maxY:
            if direction == 0:
                for i in range(y, maxY+1):
                    matrix[x][i] = val
                    val += 1
                x += 1
            elif direction == 1:
                for i in range(x, maxX+1):
                    matrix[i][maxY] = val
                    val += 1
                maxY -= 1
            elif direction == 2:
                for i in range(maxY, y-1, -1):
                    matrix[maxX][i] = val
                    val += 1
                maxX -= 1
            elif direction == 3:
                for i in range(maxX, x-1, -1):
                    matrix[i][y] = val
                    val += 1
                y += 1
            direction = (direction + 1) % 4
        return matrix

    def generateMatrix_2nd_best_speed(self, n: int) -> List[List[int]]:
        matrix = [[None] * n for _ in range(n)]
        r_min = c_min = 0
        r_max = c_max = n - 1
        val = 1
        while r_min <= r_max and c_min <= c_max:
            i = r_min
            for j in range(c_min, c_max+1):
                matrix[i][j] = val
                val += 1
            r_min += 1
            j = c_max
            for i in range(r_min, r_max+1):
                matrix[i][j] = val
                val += 1
            c_max -= 1
            i = r_max
            for j in range(c_max, c_min-1, -1):
                matrix[i][j] = val
                val += 1
            r_max -= 1
            j = c_min
            for i in range(r_max, r_min-1, -1):
                matrix[i][j] = val
                val += 1
            c_min += 1
        return matrix

    def generateMatrix_3rd__best_speed(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        right, down, left, up, i, j, count = True, False, False, False, 0, 0, 1
        while count <= n*n:
            if right:
                matrix[i][j] = count
                if j + 1 < n and matrix[i][j+1] == 0:
                    j += 1
                else:
                    i, right, down = i + 1, False, True
            elif down:
                matrix[i][j] = count
                if i + 1 < n and matrix[i+1][j] == 0:
                    i += 1
                else:
                    j, down, left = j - 1, False, True
            elif left:
                matrix[i][j] = count
                if j - 1 > -1 and matrix[i][j-1] == 0:
                    j -= 1
                else:
                    i, left, up = i - 1, False, True
            elif up:
                matrix[i][j] = count
                if i - 1 > -1 and matrix[i-1][j] == 0:
                    i -= 1
                else:
                    j, up, right = j + 1, False, True
            count += 1
        return matrix

    def generateMatrix_best_memory(self, n: int) -> List[List[int]]:
        res = []
        num = 1
        row = 0
        col = 0
        for i in range(n):
            res.append([0] * n)
        while not num > n * n:
            while col < n and res[row][col] == 0:
                res[row][col] = num
                num += 1
                col += 1
            col -= 1
            row += 1
            while row < n and res[row][col] == 0:
                res[row][col] = num
                num += 1
                row += 1
            row -= 1
            col -= 1
            while col >= 0 and res[row][col] == 0:
                res[row][col] = num
                num += 1
                col -= 1
            col += 1
            row -= 1
            while row >= 0 and res[row][col] == 0:
                res[row][col] = num
                num += 1
                row -= 1
            row += 1
            col += 1
        return res
