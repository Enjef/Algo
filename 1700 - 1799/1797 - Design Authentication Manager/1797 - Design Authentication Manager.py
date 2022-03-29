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


class AuthenticationManager_best_speed:
    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.tokens = OrderedDict()
        
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.ttl
                
    def purgeExpired(self, currentTime: int) -> None:
        k = 0
        for ttl in self.tokens.values():
            if ttl > currentTime:
                break
            k += 1
        while k > 0:
            self.tokens.popitem(last=False)
            k -= 1

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.purgeExpired(currentTime)
        if tokenId in self.tokens:
            self.tokens[tokenId] = currentTime + self.ttl
            self.tokens.move_to_end(tokenId)
            
    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.purgeExpired(currentTime)
        return len(self.tokens)


class AuthenticationManager_2nd_best_speed:
    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.cache = OrderedDict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.cache[tokenId] = currentTime + self.ttl
        
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.cache:
            return
        expiryTime = self.cache[tokenId]
        if expiryTime > currentTime:
            self.cache[tokenId] = currentTime + self.ttl
            self.cache.move_to_end(tokenId)
        
    def countUnexpiredTokens(self, currentTime: int) -> int:
        while self.cache and next(iter(self.cache.values())) <= currentTime:
            self.cache.popitem(last=False)
        return len(self.cache)


class AuthenticationManager_best_memory:
    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        oldTime = self.tokens.get(tokenId)
        if not oldTime or currentTime - oldTime >= self.timeToLive:
            return
        self.tokens[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        sum = 0
        for item in self.tokens:
            print(self.tokens[item])
            if currentTime - self.tokens[item] < self.timeToLive:
                sum += 1
        return sum
