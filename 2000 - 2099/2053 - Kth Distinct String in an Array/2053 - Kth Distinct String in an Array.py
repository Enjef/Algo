class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str: # 94.95% 74.15%
        counter = {}
        for string in arr:
            counter[string] = counter.get(string, 0) + 1
        for el in arr:
            if counter[el] == 1:
                if k > 1:
                    k -= 1
                else:
                    return el
        return ''

    def kthDistinct_best_speed(self, arr: List[str], k: int) -> str:
        count = collections.Counter(arr)
        for i in range(len(arr)):
            if count[arr[i]] == 1:
                k -= 1
                if k == 0:
                    return arr[i]
        return ''

    def kthDistinct_memory_best(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        c = [k for k,v in c.items() if v == 1]
        if len(c)>=k:
            return c[k-1]
        return ''
