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

