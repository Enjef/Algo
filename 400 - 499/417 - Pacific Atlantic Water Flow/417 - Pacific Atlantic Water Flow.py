class Solution:
    def pacificAtlantic(self, heights):  # 10.09% 5.46%
        def dfs(row, col, prev, seen):
            if (row, col) in mem:
                return mem[(row, col)]
            if (
                not(-1 < row < m and -1 < col < n) or
                heights[row][col] > prev or (row, col) in seen):
                    return set()
            cur = set()
            seen.add((row, col))
            if row == 0 or col == 0:
                cur.add('pac')
            if row == m-1 or col == n-1:
                cur.add('atl')
            cur_height = heights[row][col]
            if (
                -1 < row-1 < m and -1 < col < n and
                heights[row-1][col] <= cur_height and
                (row-1, col) not in seen):
                    cur.update(dfs(row-1, col, cur_height, seen))
            if (
                -1 < row < m and -1 < col-1 < n and
                heights[row][col-1] <= cur_height and
                (row, col-1) not in seen):
                    cur.update(dfs(row, col-1, cur_height, seen))
            if (
                -1 < row+1 < m and -1 < col < n and
                heights[row+1][col] <= cur_height and
                (row+1, col) not in seen):
                    cur.update(dfs(row+1, col, cur_height, seen))
            if (
                -1 < row < m and -1 < col+1 < n and
                heights[row][col+1] <= cur_height and
                (row, col+1) not in seen):
                    cur.update(dfs(row, col+1, cur_height, seen))
            return cur

        m, n = len(heights), len(heights[0])
        mem = {}
        for i in range(m):
            for j in range(n):
                mem[(i, j)] = dfs(i, j, float('inf'), set())
        return set([x for x in mem if len(mem[x]) == 2])


class Solution_v2:  # 72.60% 45.71%
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(out, stack):
            seen = set()
            while stack:
                temp = []
                while stack:
                    row, col = stack.pop()
                    for i in range(4):
                        y = row+dirs[i][0]
                        x = col+dirs[i][1]
                        if (
                            -1<y<m and -1<x<n and (y, x) not in seen and
                            heights[y][x] >= heights[row][col]):
                                seen.add((y, x))
                                stack.append((y, x))
                                out.add((y, x))
        
        m, n = len(heights), len(heights[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pac = set()
        atl = set()
        pac_stack = []
        atl_stack = []
        for i in range(n):
            pac_stack.append((0, i))
            pac.add((0, i))
            atl_stack.append((m-1, i))
            atl.add((m-1, i))
        for i in range(m):
            pac_stack.append((i, 0))
            pac.add((i, 0))
            atl_stack.append((i, n-1))
            atl.add((i, n-1))
        bfs(pac, pac_stack)
        bfs(atl, atl_stack)
        return pac & atl


class Solution_best_speed:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return []
        m,n = len(matrix), len(matrix[0])
        #Pacific Ocean
        OPEN = set([(0,y) for y in range(n)] + [(x,0) for x in range(m)])
        CLOSE = set()
        while OPEN:
            x,y = OPEN.pop()
            CLOSE.add((x,y))
            temp = matrix[x][y]
            if x > 0 and matrix[x-1][y] >= temp:
                if (x-1,y) not in CLOSE:
                    OPEN.add((x-1,y))
            if y > 0 and matrix[x][y-1] >= temp:
                if (x,y-1) not in CLOSE:
                    OPEN.add((x,y-1))
            if x < m-1 and matrix[x+1][y] >= temp:
                if (x+1,y) not in CLOSE:
                    OPEN.add((x+1,y))
            if y < n-1 and matrix[x][y+1] >= temp:
                if (x,y+1) not in CLOSE:
                    OPEN.add((x,y+1))
        toPacific = CLOSE
        #Atlantic Ocean
        OPEN = set([(m-1,y) for y in range(n)] + [(x,n-1) for x in range(m)])
        CLOSE = set()
        while OPEN:
            x,y = OPEN.pop()
            CLOSE.add((x,y))
            temp = matrix[x][y]
            if x > 0 and matrix[x-1][y] >= temp:
                if (x-1,y) not in CLOSE:
                    OPEN.add((x-1,y))
            if y > 0 and matrix[x][y-1] >= temp:
                if (x,y-1) not in CLOSE:
                    OPEN.add((x,y-1))
            if x < m-1 and matrix[x+1][y] >= temp:
                if (x+1,y) not in CLOSE:
                    OPEN.add((x+1,y))
            if y < n-1 and matrix[x][y+1] >= temp:
                if (x,y+1) not in CLOSE:
                    OPEN.add((x,y+1))
        toAtlantic = CLOSE
        ret = map(list, toPacific & toAtlantic)
        return ret


class Solution_best_memory:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row,col = len(heights), len(heights[0])
        dirct = [(0,1),(0,-1),(1,0),(-1,0)]
        output = set()
        def pacific(x,y,visited):
            if (x,y) in output or x == 0 or y == 0:
                return True
            visited.add((x,y))
            h = heights[x][y]
            for dx,dy in dirct:
                if (0<=x+dx<row and 0<=y+dy<col and (x+dx,y+dy) not in visited
                   and h >= heights[x+dx][y+dy]):
                    if pacific(x+dx,y+dy,visited):
                        return True
            visited.remove((x,y))
            return False
        def atlantic(x,y,visited):
            if (x,y) in output or x == row-1 or y == col-1:
                return True
            visited.add((x,y))
            h = heights[x][y]
            for dx,dy in dirct:
                if (0<=x+dx<row and 0<=y+dy<col and (x+dx,y+dy) not in visited
                   and h >= heights[x+dx][y+dy]):
                    if atlantic(x+dx,y+dy,visited):
                        return True
            visited.remove((x,y))
            return False
        
        for i in range(row):
            for j in range(col):
                if pacific(i,j,set()) and atlantic(i,j,set()):
                    output.add((i,j))
        return output
