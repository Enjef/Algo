class Solution:
    def flipAndInvertImage_my(
            self,
            image: List[List[int]]) -> List[List[int]]:  # 61.84% 58.13%
        for i in range(len(image)):
            row = image[i][::-1]
            image[i] = [0 if x == 1 else 1 for x in row]
        return image

    def flipAndInvertImage_mock(
            self,
            image: List[List[int]]) -> List[List[int]]:  # 61.84% 55.13%
        n = len(image)
        new = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new[i][n-1-j] = 0 if image[i][j] else 1
        return new

    def flipAndInvertImage_s_to_best(self, image):
        for i in range(len(image)):
            image[i] = list(reversed(image[i]))
        for i in range(len(image)):
            image[i] = [c ^ 1 for c in image[i]]
        return image

    def flipAndInvertImage_best_speed(
            self,
            A: List[List[int]]) -> List[List[int]]:
        return [[1 ^ i for i in reversed(row)] for row in A]

    def flipAndInvertImage_best_memory(
            self,
            image: List[List[int]]) -> List[List[int]]:
        for i in range (len(image)):
            image[i] = image[i][::-1]
            for j in range (len(image[i])):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image
