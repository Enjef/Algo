class Solution:
    def flipAndInvertImage_my(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            row = image[i][::-1]
            image[i] = [0 if x == 1 else 1 for x in row]
        return image

    def flipAndInvertImage_s_to_best(self, image):  # best with map+lambda
        for i in range(len(image)):
            image[i] = list(reversed(image[i]))
        for i in range(len(image)):
            image[i] = [c ^ 1 for c in image[i]]
        return image
