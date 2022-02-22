class CombinationIterator:  # 15.20% 51.98%

    def __init__(self, characters: str, combinationLength: int):
        self.comb = []

        def generate(cur, arr):
            if len(cur) == combinationLength:
                self.comb.append(cur)
                return
            for i, char in enumerate(arr):
                generate(cur+arr[i], arr[i+1:])
        self.has_next = None
        generate('', characters)

    def next(self) -> str:
        if self.has_next:
            temp = self.has_next
            self.has_next = None
            return temp
        return self.comb.pop(0)

    def hasNext(self) -> bool:
        if self.has_next:
            return True
        if not self.comb:
            return False
        self.has_next = self.comb.pop(0)
        return True


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

class CombinationIterator_v2:  # 76.29% 51.98%

    def __init__(self, characters: str, combinationLength: int):
        self.comb = []

        def generate(cur, arr):
            if len(cur) == combinationLength:
                self.comb.append(cur)
                return
            for i in range(len(arr)):
                generate(cur+arr[i], arr[i+1:])
        generate('', characters)
        self.comb.sort(reverse=True)

    def next(self) -> str:
        return self.comb.pop()

    def hasNext(self) -> bool:
        if not self.comb:
            return False
        return True


class CombinationIterator_best_speed:

    def __init__(self, characters: str, combinationLength: int):
        self.char = characters
        self.l = combinationLength
        self.path = characters[:combinationLength]
        self.stack = [x for x in range(combinationLength)]

    def next(self) -> str:
        tmp = self.path
        if (self.stack[0] == (len(self.char) - self.l)):
            self.path = None
            return tmp
        curr = self.stack.pop() + 1
        end = len(self.char) - 1
        i = 1
        while curr > end:
            curr = self.stack.pop() + 1
            end -= 1
            i += 1
        for j in range(i):
            self.stack.append(curr + j)
        self.path = self.path[:self.l - i] + self.char[curr:curr+i]
        return tmp

    def hasNext(self) -> bool:
        return self.path != None


class CombinationIterator_best_memory:

    def __init__(self, characters: str, combinationLength: int):
        self.n = len(characters)
        self.k = combinationLength
        self.nums = list(range(self.k))
        self.chars = characters
        self.has_next = True

    def next(self) -> str:
        self.curr = [self.chars[i] for i in self.nums]
        for j in range(self.k - 1, -1, -1):
            if self.nums[j] != self.n + j - self.k:
                break
        else:
            self.has_next = False
        if self.has_next:
            self.nums[j] += 1
            for m in range(j + 1, self.k):
                self.nums[m] = self.nums[m - 1] + 1
        return ''.join(self.curr)

    def hasNext(self) -> bool:
        return self.has_next
