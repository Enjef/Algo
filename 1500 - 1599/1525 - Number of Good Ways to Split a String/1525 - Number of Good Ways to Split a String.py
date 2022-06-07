class Solution:
    def numSplits(self, s: str) -> int:  # 5.07% 65.04%
        d_left = {i: 0 for i in set(s)}
        d_right = Counter(s)
        n = len(s)
        count = 0
        for char in s:
            d_left[char] += 1
            d_right[char] -= 1
            if len([x for x in d_left if d_left[x]]) == len([x for x in d_right if d_right[x]]):
                count += 1
        return count

    def numSplits_best_speed(self, s: str) -> int:
        length = len(s)
        if length ==2:
            return 1
        if length == 1:
            return 0
        first = {}
        second = {}
        for i, character in enumerate(s):
            if character not in first:
                first[character] = i
            second[character] = i
        indices = list(first.values()) + list(second.values())
        indices.sort()
        middle = len(indices) //2
        return indices[middle] - indices[middle-1]
