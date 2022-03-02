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
