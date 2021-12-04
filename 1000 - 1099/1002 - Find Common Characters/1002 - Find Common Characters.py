class Solution:
    def commonChars(self, words: List[str]) -> List[str]:  # 94.17% 33.20%
        first = {}
        for char in words.pop():
            first[char] = first.get(char, 0) + 1
        for word in words:
            for char in first.copy():
                if char not in word or first[char] == 0:
                    first.pop(char)
                elif word.count(char) < first[char]:
                    first[char] = word.count(char)
        return [
            el for tup in [[key]*value for key, value in first.items()] for
            el in tup
        ]

    def commonChars_ext(self, words: List[str]) -> List[str]:  # 98.57% 33.20%
        first = {}
        for char in words.pop():
            first[char] = first.get(char, 0) + 1
        for word in words:
            for char in first.copy():
                if char not in word or first[char] == 0:
                    first.pop(char)
                elif word.count(char) < first[char]:
                    first[char] = word.count(char)
        out = []
        [out.extend(list(key*value)) for key, value in first.items()]
        return out

    def commonChars_mock(self, words: List[str]) -> List[str]: # 98.34% 29.90%
        sets = [set(word) for word in words]
        intesection = sets[0]
        for i in range(len(sets)):
            intesection &= sets[i]
        out = []
        for char in intesection:
            amt = min([word.count(char) for word in words])
            out += [char] * amt
        return out

    def commonChars_best_speed(self, words: List[str]) -> List[str]:
        pattern = words[0]
        for wrd in words:
            for ch in pattern:
                if ch in wrd:
                    wrd = wrd.replace(ch, '', 1)
                else:
                    pattern = pattern.replace(ch, '', 1)
        return list(pattern)

    def commonChars_best_memory(self, words: List[str]) -> List[str]:
        tmp = collections.Counter(words[0])
        l = []
        for i in range(1,len(words)):
            tmp = tmp & collections.Counter(words[i])
        for j in tmp:
            v = tmp[j]
            while(v):
                l.append(j)
                v -= 1
        return l
