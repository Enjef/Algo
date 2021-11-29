class MyHashMap_ds_2_day_2:

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

class MyHashMap_best_speed:

    def __init__(self):
        self.d = dict()

    def put(self, key: int, value: int) -> None:
        self.d[key] = value

    def get(self, key: int) -> int:
        if key in self.d.keys():
            return self.d[key]
        return -1

    def remove(self, key: int) -> None:
        if key in self.d.keys():
            del self.d[key]

class MyHashMap_best_memory:

    def __init__(self):
        self.map = []

    def put(self, key: int, value: int) -> None:
        for element in self.map:
            if element[0] == key:
                element[1] = value
                return 
        self.map.append([key, value])                        

    def get(self, key: int) -> int:
        for element in self.map:
            if element[0] == key:
                return element[1]                             
        return -1

    def remove(self, key: int) -> None:
        # return [value for value in the_list if value != val]
        for element in self.map:
            if element[0] == key:                
                self.map.remove(element)  

class MyHashMap_2nd_best_memory:

    def __init__(self):
        self.array = []
        self.BUCKET_SIZE = 10
        for _ in range(self.BUCKET_SIZE):
            self.array.append([])
            

    def put(self, key: int, value: int) -> None:
        bucket_idx = hash(key) % self.BUCKET_SIZE
        # See if bucket is there
        found = False
        for idx, (item, _) in enumerate(self.array[bucket_idx]):
            if item == key:
                self.array[bucket_idx][idx] = (key, value)
                found = True
                break
        if found == False:
            self.array[bucket_idx].append((key, value))
        return None

    def get(self, key: int) -> int:
        bucket_idx = hash(key) % self.BUCKET_SIZE
        # See if bucket is there
        found = False
        for idx, (item, value) in enumerate(self.array[bucket_idx]):
            if item == key:
                return value
        if found == False:
            return -1

    def remove(self, key: int) -> None:
        bucket_idx = hash(key) % self.BUCKET_SIZE
        # See if bucket is there
        for idx, (item, value) in enumerate(self.array[bucket_idx]):
            if item == key:
                del self.array[bucket_idx][idx]
                break
        return None
