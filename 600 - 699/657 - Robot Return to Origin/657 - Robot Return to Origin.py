class Solution:
    def judgeCircle(self, moves: str) -> bool:  # 26.96% 19.43%
        coord = [0, 0]
        for move in moves:
            if move == 'U':
                coord[0] -= 1
            if move == 'D':
                coord[0] += 1
            if move == 'L':
                coord[1] -= 1
            if move == 'R':
                coord[1] += 1
        return coord == [0, 0]

    def judgeCircle_best(self, moves: str) -> bool:
        return (
            moves.count('R') == moves.count('L') and
            moves.count('U') == moves.count('D')
        )
