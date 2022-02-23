class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int: # 40.07% 23.40%
        def bfs(x, y):
            if not (-1 < x < len(mat) and -1 < y < len(mat) and not mat[x][y]):
                return
            mat[x][y] = 1
            for idx in range(4):
                bfs(x+x_way[idx], y+y_way[idx])
            return
        
        mat = [[0]*3*len(grid) for _ in range(3*len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                x, y = i*3, j*3
                if grid[i][j] == '/':
                    mat[x][y+2] = 1
                    mat[x+1][y+1] = 1
                    mat[x+2][y] = 1
                elif grid[i][j] == '\\':
                    mat[x][y] = 1
                    mat[x+1][y+1] = 1
                    mat[x+2][y+2] = 1
                    j += 1
        out = 0
        x_way = [-1, 0, 0, 1]
        y_way = [0, -1, 1, 0]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if not mat[i][j]:
                    bfs(i, j)
                    out += 1
        return out


class Solution_best_speed:
    def regionsBySlashes(self, grid) -> int:
        uf = UnionFind()
        upper = [0] * len(grid[0])
        work = [0] * len(grid[0])
        for r, row in enumerate(grid):
            upper, work = work, upper
            for c, val in enumerate(list(row)):
                if val == "\\":
                    if r > 0 and c > 0:    # Common case
                        work[c] = left       # Set the upper value to the left neighbor's value
                        left = upper[c]      # Set the left value to the upper neighbor's value
                    elif r > 0:            # Left edge of the grid
                        work[c] = uf.next()  # Allocate a new id for the upper value
                        left = upper[c]      # Set the left value to the upper neighbor's value
                    elif c > 0:            # Top edge of the grid
                        work[c] = left       # Set the upper value to the left neighbor's value
                        left = uf.next()     # Allocate a new id for the left value
                    else:                  # Upper-left corner
                        work[c] = uf.next()  # Allocate a new id for the upper value
                        left = uf.next()     # Allocate a new id for the left value
                elif val == " ":
                    if r > 0 and c > 0:    # Common case
                        work[c] = left = uf.join(upper[c], left)  # Join the upper and left values
                    elif r > 0:            # Left edge of the grid
                        work[c] = left = upper[c]   # Inherit the upper neighbor's value
                    elif c > 0:            # Top edge of the grid
                        work[c] = left              # Inherit the left neighbor's value
                    else:                  # Upper-left corner
                        work[c] = left = uf.next()  # Allocate the first id to the first square
                else:
                    if r > 0 and c > 0:    # Common case
                        uf.join(upper[c], left)  # Join the upper and left values
                    elif r == 0 and c == 0:  # Upper-left corner
                        uf.next()              # Just allocate a throway id for the small upper-left triangle
                    work[c] = left = uf.next()  # Allocate a new id for both the upper and left values
        
        # Count the number of unique parents
        return len(set(uf.find(i) for i in uf.p))


class DSU:
    def __init__(self, N):
        self.p = list(range(N))
        self.count = N

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return
        self.p[xr] = yr
        self.count -= 1


class Solution_memory_best(object):
    def regionsBySlashes(self, grid):
        N = len(grid)
        dsu = DSU(4 * N * N)
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                root = 4 * (r*N + c)
                if val in '/ ':
                    dsu.union(root + 0, root + 1)
                    dsu.union(root + 2, root + 3)
                if val in '\ ':
                    dsu.union(root + 0, root + 2)
                    dsu.union(root + 1, root + 3)

                # north/south
                if r+1 < N: dsu.union(root + 3, (root+4*N) + 0)
                # if r-1 >= 0: dsu.union(root + 0, (root-4*N) + 3)
                # east/west
                if c+1 < N: dsu.union(root + 2, (root+4) + 1)
                #if c-1 >= 0: dsu.union(root + 1, (root-4) + 2)
        return dsu.count


class Solution_3d_memory_best:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        supergraph = list([0]*(n*3) for i in range(n*3))
        count = 0
        m = n*3
        xmov = [-1,0,1,0]
        ymov = [0,-1,0,1]
        
        def dfs(a,b):
            stack = [(a,b)]
            while stack:
                x,y = stack.pop()
                supergraph[x][y] = 1
                for i in range(4):
                    xtemp = x + xmov[i]
                    ytemp = y + ymov[i]
                    if xtemp > -1 and xtemp < m and ytemp > -1 and ytemp < m:
                        if supergraph[xtemp][ytemp] == 0:
                            stack.append((xtemp,ytemp))
        
        for x in range(n):
            for y in range(n):
                if grid[x][y] == "\\":
                    supergraph[x*3][y*3] = supergraph[x*3 + 1][y*3 + 1] = supergraph[x*3 + 2][y*3 + 2] = 1
                elif grid[x][y] == "/":
                    supergraph[x*3 + 2][y*3] = supergraph[x*3 + 1][y*3 + 1] = supergraph[x*3][y*3 + 2] = 1
        for x in range(m):
            for y in range(m):
                if supergraph[x][y] != 1:
                    dfs(x,y)
                    count+=1
        return count

class UnionFind:
    def __init__(self):
        self.p = []
        self.rank = []

    def join(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return a

        if self.rank[a] >= self.rank[b]:
            self.rank[a] += self.rank[b]
            self.p[b] = a
            return a
        else:
            self.rank[b] += self.rank[a]
            self.p[a] = b
            return b

    def find(self, a):
        while a != self.p[a]:
            a = self.p[a]
        return a
            
    def next(self):
        try:
            return len(self.p)
        finally:
            self.p.append(len(self.p))
            self.rank.append(1)
