import random


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


class RandomizedSet_best_speed:
    def __init__(self):
        self.value_idx_map = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.value_idx_map:
            return False
        self.value_idx_map[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.value_idx_map:
            return False
        if len(self.values) == 1:
            del self.value_idx_map[val]
            self.values.pop()
            return True
        idx = self.value_idx_map[val]
        last_element = self.values[-1]
        self.values[-1], self.values[idx] = val, last_element
        self.value_idx_map[last_element] = idx
        del self.value_idx_map[val]
        self.values.pop()
        return True
        
    def getRandom(self) -> int:
        idx = int(random.random() * len(self.values))
        return self.values[idx]

class RandomizedSet_best_memory:
    def __init__(self):
        self.dict = {}
        self.list = []
        
    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val in self.dict:
            last_element, i_curr_element = self.list[-1], self.dict[val]
            self.list[i_curr_element], self.dict[last_element] = last_element, i_curr_element
            self.list.pop()
            del self.dict[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.list)
