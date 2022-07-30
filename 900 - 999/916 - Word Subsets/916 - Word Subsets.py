class Solution:
    #  50.17% 6.51% (72.64% 7.49%)
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        test = [Counter(word) for word in words1]
        target = {}
        for word in words2:
            temp = Counter(word)
            for char in temp:
                target[char] = max(target.get(char, 0), temp[char])
        out = []
        for i, word in enumerate(test):
            for char in target:
                if char not in word or target[char] > word[char]:
                    break
            else:
                out.append(i)
        return [words1[i] for i in out]
