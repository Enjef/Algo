class MyHashMap:

    def __init__(self):  # 18.14% 96.88%
        self.key = []
        self.value = []

    def put(self, key: int, value: int) -> None:
        if key in self.key:
            self.value[self.key.index(key)] = value
        else:
            self.key.append(key)
            self.value.append(value)

    def get(self, key: int) -> int:
        if key not in self.key:
            return -1
        return self.value[self.key.index(key)]

    def remove(self, key: int) -> None:
        if key in self.key:
            self.value.pop(self.key.index(key))
            self.key.remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
