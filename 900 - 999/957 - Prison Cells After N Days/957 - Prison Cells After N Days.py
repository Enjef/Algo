class Solution:
    def prisonAfterNDays(
            self,
            cells: List[int],
            n: int) -> List[int]:  # 86.79% 32.91%
        n %= 14
        if n == 0:
            n = 14
        for _ in range(n):
            new = cells[:]
            for i in range(1, len(cells)-1):
                if cells[i-1] == cells[i+1]:
                    new[i] = 1
                else:
                    new[i] = 0
            new[0] = new[-1] = 0
            cells = new
        return cells

    def prisonAfterNDays_best_speed(
            self,
            cells: List[int],
            n: int) -> List[int]:
        for i in range((n -1) % 14 + 1):
            res = [0]
            for i in range(1, 7):
                if cells[i-1] == cells[i+1]:
                    res.append(1)
                else:
                    res.append(0)
            res.append(0)
            cells = res 
        return res

    def prisonAfterNDays_best_memory(
            self,
            cells: List[int],
            n: int) -> List[int]:
        memo = {tuple(cells):0}
        i = 1
        cycle = False
        while i < n + 1:
            next_cells = deepcopy(cells)
            next_cells[0] = next_cells[7] = 0
            for c in range(1, 7):
                if cells[c-1] == cells[c+1]:
                    next_cells[c] = 1
                else:
                    next_cells[c] = 0
            if memo.get(tuple(next_cells)) and not cycle:
                cycle = True
                cycle_start = memo.get(tuple(next_cells))
                i += ((n-i) // (i-cycle_start)) * (i-cycle_start)
            memo[tuple(next_cells)] = i
            cells = next_cells
            i += 1
        return cells
