class Solution:
    def floodFill(
            self,
            image: List[List[int]],
            sr: int,
            sc: int,
            newColor: int) -> List[List[int]]:
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

    def floodFill_second_run(
            self,
            image: List[List[int]],
            sr: int,
            sc: int,
            newColor: int) -> List[List[int]]:  # 72.15% 97.97%
        target = image[sr][sc]
        if target == newColor:
            return image
        stack = [(sr, sc)]
        while stack:
            i, j = stack.pop()
            if (
                    0 <= i < len(image) and
                    0 <= j < len(image[0]) and
                    image[i][j] == target):
                image[i][j] = newColor
                stack.extend([(i-1, j), (i+1, j), (i, j-1), (i, j+1)])
        return image
