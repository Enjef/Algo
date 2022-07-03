class Solution:
    # 8.05% 65.58%
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def bfs(y, x, target):
            if not(-1 < y < m and -1 < x < n and image[y][x] == target):
                return
            image[y][x] = newColor
            for idx in range(4):
                bfs(y+y_dir[idx], x+x_dir[idx], target)
            return

        m, n = len(image), len(image[0])
        x_dir, y_dir = [0, 0, -1, 1], [-1, 1, 0, 0]
        if image[sr][sc] == newColor:
            return image
        bfs(sr, sc, image[sr][sc])
        return image
