class Solution:
    def isPrefixOfWord(
            self,
            sentence: str,
            searchWord: str) -> int:  # 7.28% 44.92%
        words = sentence.split()
        for i in range(len(words)):
            if searchWord in words[i] and words[i].startswith(searchWord):
                return i+1
        return -1

    def isPrefixOfWord_best_speed(
            self,
            sentence: str,
            searchWord: str) -> int:  # 79.40% 13.05%
        ret = -1
        words = sentence.split()
        for j in range(len(words)):
            w = words[j]
            if len(searchWord) <= len(w):
                a = True
                for i in range(len(searchWord)):
                    if w[i] != searchWord[i]:
                        a = False
                        break
                if a:
                    ret = j + 1
                    return ret
        return ret

    def isPrefixOfWord_best_memory(
            self,
            sentence: str,
            searchWord: str) -> int:
        ss = sentence.split(" ")
        for i, v in enumerate(ss):
            if v.find(searchWord) == 0:
                return i+1
        return -1
