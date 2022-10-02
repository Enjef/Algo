class LUPrefix:

    def __init__(self, n: int):
        self.videos = [0] * n
        self.idx = -1

    def upload(self, video: int) -> None:
        self.videos[video-1] = 1
        while self.idx < len(self.videos)-1 and self.videos[self.idx+1]:
            self.idx += 1

    def longest(self) -> int:
        if self.idx == -1:
            return 0
        return self.idx + 1


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
