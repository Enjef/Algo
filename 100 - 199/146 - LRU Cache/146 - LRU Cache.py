class LRUCache:  # 8.45% 66.82%

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.stack.append(self.stack.pop(self.stack.index(key)))
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.stack.append(self.stack.pop(self.stack.index(key)))
        elif key not in self.cache and len(self.stack) < self.capacity:
            self.cache[key] = value
            self.stack.append(key)
        else:
            self.cache.pop(self.stack.pop(0))
            self.cache[key] = value
            self.stack.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
