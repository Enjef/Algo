class Solution:
    def mostCommonWord(
            self,
            paragraph: str,
            banned: List[str]) -> str:  # 88.45% 73.78%
        word = ''
        count = {}
        for char in paragraph:
            if char.isalpha():
                word += char.lower()
            else:
                if word and word not in banned:
                    count[word] = count.get(word, 0) + 1
                word = ''
        if word:
            count[word] = count.get(word, 0) + 1
        return max(count, key=count.get)

    def mostCommonWord_best_speed(
            self,
            paragraph: str,
            banned: List[str]) -> str:
        ns = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        words = ns.split()
        word_count = defaultdict(int)
        banned_words = set(banned)
        for word in words:
            if word not in banned_words:
                word_count[word] += 1
        return max(word_count.items(), key=operator.itemgetter(1))[0]

    def mostCommonWord_best_memory(
            self,
            paragraph: str,
            banned: List[str]) -> str:
        boo = "!?',;."
        breaks = {}
        for bo in boo:
            breaks[bo] = 1
        breaks[' '] = 1
        B = {}
        for word in banned:
            B[word] = 1
        ct = 0
        s = ""
        count = {}
        while ct < len(paragraph):
            if paragraph[ct] not in breaks:
                s = s + paragraph[ct]
            else:
                s = s.lower()
                if s in count and s not in banned and s != "":
                    count[s] = count[s] + 1
                elif s not in banned and s != "":
                    count[s] = 1
                s = ""
            ct = ct + 1
        s = s.lower()
        if s in count and s not in banned and s != "":
            count[s] = count[s] + 1
        elif s not in banned and s != "":
            count[s] = 1
        return max(count, key=count.get)
