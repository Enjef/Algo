class AuthenticationManager:
    def __init__(self, timeToLive: int):  # 73.57% 15.71%
        self.tokens = dict()
        self.time_to_live = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.time_to_live
        return

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.tokens or currentTime >= self.tokens[tokenId]:
            return
        self.tokens[tokenId] = currentTime + self.time_to_live
        return

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return sum([1 for x in self.tokens.values() if x > currentTime])


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
