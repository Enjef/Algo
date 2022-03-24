class Solution:
    def checkAlmostEquivalent(self, word1, word2):  # 29.67% 98.82%
        total = set(word1) | set(word2)
        first = dict(zip(total, [0]*len(total)))
        second = first.copy()
        for char in word1:
            first[char] += 1
        for char in word2:
            second[char] += 1
        for key in first:
            if abs(first[key]-second[key]) > 3:
                return False
        return True

    def checkAlmostEquivalent_best_speed(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)
        max_ = 0
        for k in count1:
            if k in count2:
                max_ = max(max_, abs(count1[k] - count2[k]))
            else:
                max_ = max(max_, count1[k])
        for k in count2:
            if k not in count1:
                max_ = max(max_, count2[k])
        return max_ <= 3

    def checkAlmostEquivalent_best_memory(self, word1, word2):
        count=Counter(word1)
        for ch in word2:
            count[ch]-=1
        return max(abs(val) for val in count.values())<=3
