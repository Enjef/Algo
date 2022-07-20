class Solution:
    # 37.93% 16.33% (56.18% 16.33%)
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = defaultdict(list)
        result = 0
        for i, char in enumerate(s):
            d[char].append(i)
        for word in words:
            cur = -1
            for char in word:
                idx = bisect_right(d[char], cur)
                if idx < len(d[char]) and d[char][idx] > cur:
                    cur = d[char][idx]
                else:
                    break
            else:
                result += 1
        return result

    # 37.61% 98.31% (71.83% 51.10%)
    def numMatchingSubseq_v2(self, s: str, words: List[str]) -> int:  
        d = defaultdict(list)
        result = 0
        for word in words:
            d[word[0]].append(word)
        for char in s:
            new = []
            for word in d[char]:
                if len(word) == 1:
                    result += 1
                else:
                    if word[1] == char:
                        new.append(word[1:])
                    else:
                        d[word[1]].append(word[1:])
            d[char] = new
        return result

    def numMatchingSubseq_best_speed(self, s: str, words: List[str]) -> int:
        word_count = dict()
        for word in words:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
        count = 0
        for word in word_count:
            i = 0
            for char in word:
                i = s.find(char, i) + 1
                if not i:
                    break
            if i:
                count += word_count[word]
        return count


class Solution_best_memory:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def subs(a, b):
            m = len(a)
            n = len(b)
            i, j = 0, 0
            while(i < m):
                if a[i] == b[j]:
                    if j == n-1:
                        return True
                    j += 1
                    i += 1
                else:
                    i += 1
            return False
        out = 0
        cnt = Counter(words)
        for i in cnt:
            if subs(s, i):
                out += cnt[i]
        return out
