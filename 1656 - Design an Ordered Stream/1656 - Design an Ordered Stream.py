class OrderedStream:

    def __init__(self, n: int):
        self.s = ['']*n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:  # 79.47 %
        self.s[idKey-1] = value
        if not self.s[self.ptr]:
            return []
        else:
            left = self.ptr
            while self.s[self.ptr]:
                self.ptr += 1
                if self.ptr == len(self.s):
                    break
            return self.s[left: self.ptr]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)


'''
    def __init__(self, n: int):
        self.a, self.i = [False]*(n+1),  0
    def insert(self, idKey: int, value: str) -> List[str]:
        a, i, self.a[idKey-1] = self.a, self.i, value
        if a[i]:
            self.i = self.a.index(False,i+1)
            return self.a[i:self.i]
'''
