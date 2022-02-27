class Solution:  # 41.13% 54.43%
    def __init__(self):
        self.good = True

    def countSubIslands(self, grid1, grid2) -> int:
        def bfs(row, col):
            if not(-1 < row < m and -1 < col < n and grid2[row][col]):
                return
            if not grid1[row][col]:
                self.good = False
            grid2[row][col] = 0
            bfs(row, col-1)
            bfs(row, col+1)
            bfs(row-1, col)
            bfs(row+1, col)
            return

        m, n = len(grid1), len(grid1[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j]:
                    self.good = True
                    bfs(i, j)
                    if self.good:
                        res += 1
        return res


class Solution_best_speed:
    def countSubIslands(self, grid1, grid2) -> int:
        m = len(grid1)
        n = len(grid1[0])
        cont = 0
        for k in range(m):
            for j in range(n):
                if grid2[k][j] == 1:
                    l = [[k, j]]
                    grid2[k][j] = 3
                    cur = 1
                    while l != []:
                        l1 = []
                        for i in l:
                            r = i[0]
                            c = i[1]
                            if grid1[r][c] == 0:
                                cur = 0
                            if r != 0:
                                if grid2[r-1][c] == 1:
                                    l1.append([r-1, c])
                                    grid2[r-1][c] = 2
                            if r != m-1:
                                if grid2[r+1][c] == 1:
                                    l1.append([r+1, c])
                                    grid2[r+1][c] = 2
                            if c != 0:
                                if grid2[r][c-1] == 1:
                                    l1.append([r, c-1])
                                    grid2[r][c-1] = 2
                            if c != n-1:
                                if grid2[r][c+1] == 1:
                                    l1.append([r, c+1])
                                    grid2[r][c+1] = 2
                        l = l1
                    cont += cur
        return cont


class Solution_2nd_best_speed:
    def countSubIslands(self, grid1, grid2) -> int:
        global m
        global n
        m = len(grid2)
        n = len(grid2[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and grid1[i][j] == 1:
                    flag = [True]
                    self.dfs(i, j, grid2, grid1, flag)
                    if flag[0] == True:
                        count += 1
        return count
    
    def dfs(self, i, j, grid2, grid1, flag):
        grid2[i][j] = 2
        if grid1[i][j] == 0:
            flag[0] = False
        if j > 0 and grid2[i][j - 1] == 1:
            self.dfs(i, j - 1, grid2, grid1, flag)
        if j < n - 1 and grid2[i][j + 1] == 1:
            self.dfs(i, j + 1, grid2, grid1, flag)
        if i > 0 and grid2[i - 1][j] == 1:
            self.dfs(i - 1, j, grid2, grid1, flag)
        if i < m - 1 and grid2[i + 1][j] == 1:
            self.dfs(i + 1, j, grid2, grid1, flag)
        return


class Solution_best_memory:
    def countSubIslands(self, grid1, grid2) -> int:
        nrow = len(grid2)
        ncol = len(grid2[0])
        
        def bfs(i,j):
            dq = deque([(i,j),])
            grid2[i][j] = -1
            res = True
            while dq:
                ii, jj = dq.popleft()
                for r, c in [(ii+1,jj),(ii-1,jj),(ii,jj+1),(ii,jj-1)]: 
                    if r>=0 and c>=0 and r<nrow and c<ncol and grid2[r][c]==1:
                        if grid1[r][c] != 1:
                            res = False
                        dq.append((r,c)) 
                        grid2[r][c] = -1
            return res
        cnt = 0
        for i in range(nrow):
            for j in range(ncol):
                if grid2[i][j] == 1 and grid1[i][j] == 1:
                    if bfs(i,j):
                        cnt += 1
        return cnt
