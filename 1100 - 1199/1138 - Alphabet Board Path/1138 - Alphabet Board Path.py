class Solution:
    def alphabetBoardPath(self, target: str) -> str:  # 5.15% 5.15%
        def bfs(tar):
            stack = [(self.i, self.j, [])]
            while stack:
                new = []
                for x, y, cur_path in stack:
                    for xx, yy, step in dirs:
                        cur_x, cur_y = x+xx, y+yy
                        if not(
                            (cur_x == 5 and cur_y == 0) or
                                (-1 < cur_x < n and -1 < cur_y < m)):
                            continue
                        if board[cur_x][cur_y] == tar:
                            self.i, self.j = cur_x, cur_y
                            path.extend(cur_path+[step]+['!'])
                            return
                        new.append((cur_x, cur_y, cur_path+[step]))
                stack = new
            return -1

        board = ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy', 'z']
        n, m = 5, 5
        path = []
        self.i, self.j = 0, 0
        dirs = [(-1, 0, 'U'), (0, -1, 'L'), (0, 1, 'R'), (1, 0, 'D')]
        for char in target:
            if board[self.i][self.j] == char:
                path.append('!')
                continue
            bfs(char)
        return ''.join(path)

    def alphabetBoardPath_v2(self, target: str) -> str:  # 78.59% 39.02%
        coords = {
            'a': (0, 0),
            'b': (0, 1),
            'c': (0, 2),
            'd': (0, 3),
            'e': (0, 4),
            'f': (1, 0),
            'g': (1, 1),
            'h': (1, 2),
            'i': (1, 3),
            'j': (1, 4),
            'k': (2, 0),
            'l': (2, 1),
            'm': (2, 2),
            'n': (2, 3),
            'o': (2, 4),
            'p': (3, 0),
            'q': (3, 1),
            'r': (3, 2),
            's': (3, 3),
            't': (3, 4),
            'u': (4, 0),
            'v': (4, 1),
            'w': (4, 2),
            'x': (4, 3),
            'y': (4, 4),
            'z': (5, 0),
        }

        prev = 'a'
        path = []
        for char in target:
            x, y = coords[prev]
            xx, yy = coords[char]
            ver, hor = xx - x, yy - y
            if ver < 0:
                path.append('U'*abs(ver))
            if hor < 0:
                path.append('L'*abs(hor))
            if ver > 0:
                path.append('D'*ver)
            if hor > 0:
                path.append('R'*hor)
            path.append('!')
            prev = char
        return ''.join(path)

    def alphabetBoardPath_v3(self, target: str) -> str:  # 67.48% 98.64%
        return ''.join([''.join(['U'*(x-xx), 'L'*(y-yy), 'D'*(xx-x), 'R'*(yy-y), '!']) for (x, y), (xx, yy) in zip([(0, 0)]+[divmod(ord(char) - ord('a'), 5) for char in target], [divmod(ord(char) - ord('a'), 5) for char in target])])

    def alphabetBoardPath_v4_pairwise(self, target: str) -> str:  # 88.08% 86.99%
        return ''.join([''.join(['U'*(x-xx), 'L'*(y-yy), 'D'*(xx-x), 'R'*(yy-y), '!']) for (x, y), (xx, yy) in pairwise([(0, 0)]+[divmod(ord(char) - ord('a'), 5) for char in target])])

    def alphabetBoardPath_best_speed(self, target: str) -> str:
        board = ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy', 'z']
        da = dict()
        for i in range(len(board)):
            t = board[i]
            for j in range(len(t)):
                da[board[i][j]] = [i, j]

        r, c = 0, 0
        res = ''
        for t in target:
            nR, nC = da[t]
            row_first = True
            if r == len(board) - 1:
                row_first = False
            if row_first:
                if nC > c:
                    res += 'R' * (nC - c)
                elif nC < c:
                    res += 'L' * (c-nC)
            if nR > r:
                res += 'D' * (nR-r)
            elif nR < r:
                res += 'U' * (r-nR)
            if not row_first:
                if nC > c:
                    res += 'R' * (nC - c)
                elif nC < c:
                    res += 'L' * (c-nC)
            res += '!'
            r, c = nR, nC
        return res

    def alphabetBoardPath_3d_best_speed(self, target: str) -> str:
        cur = (0, 0)
        ans = []
        for char in target:
            val = ord(char) - ord('a')
            pos = (val // 5, val % 5)
            ans += 'L' * (cur[1] - pos[1])
            ans += 'U' * (cur[0] - pos[0])
            ans += 'R' * (pos[1] - cur[1])
            ans += 'D' * (pos[0] - cur[0])
            ans += '!'
            cur = pos
        return ''.join(ans)

    def alphabetBoardPath_best_memory(self, target: str) -> str:
        board = ['abcde', 'fghij', 'klmno', 'pqrst', 'uvwxy', 'z']
        position = {}
        for r in range(5):
            for c in range(5):
                position[board[r][c]] = (r, c)
        position[board[5][0]] = (5, 0)

        start = (0, 0)
        res = ''
        for letter in target:
            end = position[letter]
            x, y = end[0] - start[0], end[1] - start[1]
            dir1 = 'D' if x >= 0 else 'U'
            dir2 = 'R' if y >= 0 else 'L'
            if letter == 'z':
                res += dir2 * abs(y) + dir1 * abs(x) + '!'
            else:
                res += dir1 * abs(x) + dir2 * abs(y) + '!'
            start = end
        return res
