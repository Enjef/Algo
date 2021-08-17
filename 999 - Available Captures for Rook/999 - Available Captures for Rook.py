class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:  # 59.95% 61.46%
        r_index = []
        for row in range(len(board)):
            r_index = [row, board[row].index('R') if 'R' in board[row] else -1]
            if r_index[1] > -1:
                break
        horizontal = board[r_index[0]]
        vertical = [board[row][r_index[1]] for row in range(len(board[0]))]
        directions = [
            horizontal[:r_index[1]][::-1], horizontal[r_index[1]+1:],
            vertical[:r_index[0]][::-1], vertical[r_index[0]+1:]
        ]
        return sum([self.search_b(direction) for direction in directions])

    def search_b(self, arr):
        for char in arr:
            if char == 'B':
                return False
            if char == 'p':
                return True
        return False

    def numRookCaptures_best(self, board: List[List[str]]) -> int:
        rookIndex = (0, 0)
        for r in range(len(board)):
            if "R" in board[r]:
                rookIndex = (r, board[r].index("R"))
        numCaptures = 0
        for i in range(rookIndex[1]-1, -1, -1):
            if board[rookIndex[0]][i] == 'p':
                numCaptures += 1
                break
            elif board[rookIndex[0]][i] == 'B':
                break
        for i in range(rookIndex[1]+1, len(board[0])):
            if board[rookIndex[0]][i] == 'p':
                numCaptures += 1
                break
            elif board[rookIndex[0]][i] == 'B':
                break
        for i in range(rookIndex[0]-1, -1, -1):
            if board[i][rookIndex[1]] == 'p':
                numCaptures += 1
                break
            elif board[i][rookIndex[1]] == 'B':
                break
        for i in range(rookIndex[0]+1, len(board)):
            if board[i][rookIndex[1]] == 'p':
                numCaptures += 1
                break
            elif board[i][rookIndex[1]] == 'B':
                break
        return numCaptures
