class RandomizedSet:
    def __init__(self):  # 29.59% 89.08%
        self.data = set()

    def insert(self, val: int) -> bool:
        res = val not in self.data
        self.data.add(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.data
        self.data.discard(val)
        return res

    def getRandom(self) -> int:
        return random.choice(list(self.data))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
