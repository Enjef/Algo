class Solution:
    def countWords(
            self, wrds1: List[str], words2: List[str]) -> int:  # 66.40% 84.95%
        count_first = defaultdict(int)
        count_second = defaultdict(int)
        for word in wrds1:
            count_first[word] += 1
        for word in words2:
            count_second[word] += 1
        result = 0
        for word in wrds1:
            if count_first[word] == count_second[word] == 1:
                result += 1
        return result

    def countWords_best_speed(self, words1: List[str], words2: List[str]):
        D1 = {}
        for i in words1:
            if i not in D1:
                D1[i] = 1
            else:
                D1[i] += 1
        D2 = {}
        for i in words2:
            if i not in D2:
                D2[i] = 1
            else:
                D2[i] += 1
        c = 0
        for i, v in D1.items():
            if D1[i] == 1 and D2.get(i) != None:
                if D2[i] == 1:
                    c += 1
        return c

    def countWords_2nd_best_speed(self, words1: List[str], words2: List[str]):
        diff = set(words1) & set(words2)
        cnt_w = Counter(words1 + words2)
        out = 0
        for word in diff:
            if cnt_w[word] == 2:
                out += 1
        return out

    def countWords_best_memory(self, words1: List[str], words2: List[str]):
        words1_info = []
        words2_info = []
        for i in words1:
            if words1.count(i) == 1:
                words1_info.append(i)
        for i in words2:
            if words2.count(i) == 1:
                words2_info.append(i)
        return len([i for i in words1_info if i in words2_info])
