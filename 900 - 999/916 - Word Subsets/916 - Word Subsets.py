import collections


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

    # 37.14% 8.14%
    def wordSubsets_v2(self, words1: List[str], words2: List[str]) -> List[str]:
        return [a for a in words1 if not words2 - Counter(a)] if (words2 := reduce(operator.ior, [Counter(b) for b in words2])) else []

    def wordSubsets_best_speed(self, words1: List[str], words2: List[str]) -> List[str]:
        Bfreq, ans, cmax = {}, [], 0
        for word in words2:
            for char in word:
                count = word.count(char)
                if char in Bfreq:
                    diff = count - Bfreq[char]
                    if diff > 0:
                        Bfreq[char] = count
                        cmax += diff
                else:
                    Bfreq[char] = count
                    cmax += count
            if cmax > 10:
                return ans
        for word in words1:
            if len(word) < cmax:
                continue
            for char in Bfreq:
                if word.count(char) < Bfreq[char]:
                    break
            else:
                ans.append(word)
        return ans

    def getFreqOfChar(self, string):
        freq = [0] * 26
        for j in string:
            freq[ord(j)-ord('a')] += 1
        return freq

    def wordSubsets_best_memory(self, words1: List[str], words2: List[str]) -> List[str]:
        result = []
        maxCount = [0] * 26
        for word in words2:
            charFreq = self.getFreqOfChar(word)
            for j in range(26):
                maxCount[j] = max(maxCount[j], charFreq[j])

        for idx, word in enumerate(words1):
            word1CharFreq = self.getFreqOfChar(word)
            flag = True
            for i in range(26):
                if maxCount[i] > word1CharFreq[i]:
                    flag = False
                    break
            if flag:
                result.append(word)
        return result

    def wordSubsets_2nd_best_memory(self, words1: List[str], words2: List[str]) -> List[str]:
        count = collections.Counter()
        for b in words2:
            count |= collections.Counter(b)
        return [a for a in words1 if not count - Counter(a)]
