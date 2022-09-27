class Solution:
    # 75.00% 10.05% (27.34% 10.05%)
    def pushDominoes(self, dominoes: str) -> str:
        stack_left = set()
        stack_right = set()
        n = len(dominoes)
        result = list(dominoes)
        for i, direction in enumerate(dominoes):
            if direction == 'L':
                stack_left.add(i)
            if direction == 'R':
                stack_right.add(i)
        while stack_left or stack_right:
            next_left = set()
            next_right = set()
            for idx in stack_left:
                if idx-1 > -1 and result[idx-1] == '.':
                    next_left.add(idx-1)
            for idx in stack_right:
                if idx+1 < n and result[idx+1] == '.':
                    next_right.add(idx+1)
            stack_left = next_left - next_right
            for idx in stack_left:
                result[idx] = 'L'
            stack_right = next_right - next_left
            for idx in stack_right:
                result[idx] = 'R'
        return ''.join(result)

    # 47.90% 30.84% (53.51% 30.84%)
    def pushDominoes_v2(self, dominoes: str) -> str:
        return dominoes if dominoes == dominoes.replace('R.L', 'X').replace('.L', 'LL').replace('R.', 'RR').replace('X', 'R.L') else self.pushDominoes(dominoes.replace('R.L', 'X').replace('.L', 'LL').replace('R.', 'RR').replace('X', 'R.L'))

    def pushDominoes_best_speed(self, dominoes: str) -> str:
        N = len(dominoes)
        d = 'L'
        prev = -1
        s = ''
        for i in range(N):
            if dominoes[i] == 'R':
                c = 'R' if d == 'R' else '.'
                s += (i-prev-1) * c + 'R'
                prev, d = i, 'R'
            elif dominoes[i] == 'L':
                if d == 'L':
                    s += (i-prev) * 'L'
                else:
                    l1, l2 = divmod(i-prev-1, 2)
                    s += 'R'*l1 + '.'*l2 + 'L'*(l1+1)
                prev, d = i, 'L'
        s += (N-prev-1)*'R' if d == 'R' else (N-prev-1)*'.'
        return s

    def pushDominoes_4th_best_speed(self, dominoes: str) -> str:
        while True:
            new = dominoes.replace('R.L', 'S')
            new = new.replace('.L', 'LL').replace('R.', 'RR')
            if new == dominoes:
                break
            else:
                dominoes = new
        return dominoes.replace('S', 'R.L')

    def pushDominoes_best_memory(self, dominoes: str) -> str:
        while True:
            new_dominoes = dominoes.replace('R.L', '|').replace('.L', 'LL').replace('R.', 'RR').replace('|', 'R.L')
            if new_dominoes == dominoes:
                break
            else:
                dominoes = new_dominoes
        return dominoes
