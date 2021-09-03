class Solution:
    def floodFill(
            self,
            image: List[List[int]],
            sr: int,
            sc: int,
            newColor: int) -> List[List[int]]:  # 62.15% 76.11%
        target = image[sr][sc]
        if target == newColor:
            return image
        n = len(image) - 1
        m = len(image[0]) - 1
        stack = [(sr, sc)]
        while stack:
            cur = stack.pop()
            image[cur[0]][cur[1]] = newColor
            if cur[0] - 1 >= 0 and image[cur[0]-1][cur[1]] == target:
                stack.append((cur[0] - 1, cur[1]))
            if cur[0] + 1 <= n and image[cur[0] + 1][cur[1]] == target:
                stack.append((cur[0] + 1, cur[1]))
            if cur[1] - 1 >= 0 and image[cur[0]][cur[1] - 1] == target:
                stack.append((cur[0], cur[1] - 1))
            if cur[1] + 1 <= m and image[cur[0]][cur[1] + 1] == target:
                stack.append((cur[0], cur[1] + 1))
        return image

    def floodFill_sp_day_7(
            self,
            image: List[List[int]],
            sr: int,
            sc: int,
            newColor: int) -> List[List[int]]:  # 5.15% 52.79%
        tar = image[sr][sc]
        if tar == newColor:
            return image

        def helper(img, r, c, new):
            if image[r][c] == tar:
                image[r][c] = new
                if r > 0:
                    helper(image, r-1, c, new)
                if r < len(image)-1:
                    helper(image, r+1, c, new)
                if c > 0:
                    helper(image, r, c-1, new)
                if c < len(image[0])-1:
                    helper(image, r, c+1, new)
            return image
        helper(image, sr, sc, newColor)
        return image

    def floodFill_best_speed(
            self,
            image: List[List[int]],
            sr: int,
            sc: int,
            newColor: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        color = image[sr][sc]
        if image[sr][sc] == newColor:
            return image

        def dfs(sr, sc):
            if image[sr][sc] == color:
                image[sr][sc] = newColor
                if (sr-1) >= 0:
                    dfs(sr-1, sc)
                if (sr+1) < row:
                    dfs(sr+1, sc)
                if (sc-1) >= 0:
                    dfs(sr, sc-1)
                if (sc+1) < col:
                    dfs(sr, sc+1)

        dfs(sr, sc)
        return image
