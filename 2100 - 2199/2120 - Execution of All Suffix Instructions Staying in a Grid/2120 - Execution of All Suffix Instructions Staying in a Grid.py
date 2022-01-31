class Solution:
    def executeInstructions(
            self, n: int, startPos: List[int], s: str):  # 69.26% 99.44%
        def bfs(x, y, idx):
            res = 0
            for i in range(idx, len(s)):
                xx, yy = directions[s[i]]
                x += xx
                y += yy
                if not (-1 < x < n and -1 < y < n):
                    break
                res += 1
            return res
        out = []
        directions = {
            'L': (0, -1),
            'U': (-1, 0),
            'D': (1, 0),
            'R': (0, 1)
        }
        for i in range(len(s)):
            out.append(bfs(startPos[0], startPos[1], i))
        return out

    def executeInstructions_best_speed(
            self, n: int, startPos: List[int], s: str) -> List[int]:
        ans = []
        m = len(s)
        directions = {'L': [0, -1], 'R': [0, 1], 'D': [1, 0], 'U': [-1, 0]}
        l, d, r, u = startPos[1]+1, n-startPos[0], n-startPos[1], startPos[0]+1
        nextrow, nextcol = {0: m}, {0: m}
        currow, curcol = 0, 0
        for i in range(m-1, -1, -1):
            currow -= directions[s[i]][0]
            curcol -= directions[s[i]][1]
            maxstep = m - i
            if currow - u in nextrow:
                maxstep = min(maxstep, nextrow[currow - u] - i - 1)
            if currow + d in nextrow:
                maxstep = min(maxstep, nextrow[currow + d] - i - 1)
            if curcol - l in nextcol:
                maxstep = min(maxstep, nextcol[curcol - l] - i - 1)
            if curcol + r in nextcol:
                maxstep = min(maxstep, nextcol[curcol + r] - i - 1)
            nextrow[currow] = i
            nextcol[curcol] = i
            ans.append(maxstep)
        return ans[::-1]

    def executeInstructions_best_memory(
            self, n: int, start_pos: List[int], s: str) -> List[int]:
        move_table = {}
        length = len(s)
        answer = [0] * length
        for i in range(0, length):
            move = s[i]
            if move == 'R':
                tmp = [0, 1]
            elif move == 'L':
                tmp = [0, -1]
            elif move == 'D':
                tmp = [1, 0]
            else:
                tmp = [-1, 0]
            move_table[i] = tmp
        for i in range(0, length):
            cur = start_pos.copy()
            for j in range(i, length):
                tmp = move_table.get(j)
                x = cur[0] + tmp[0]
                y = cur[1] + tmp[1]
                if not (0 <= x < n and 0 <= y < n):
                    break
                answer[i] = j - i + 1
                cur = [x, y]
        return answer
