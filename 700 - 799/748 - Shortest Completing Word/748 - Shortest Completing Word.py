class Solution:
    def shortestCompletingWord(
            self, licensePlate: str, words: List[str]) -> str:  # 44.85% 81.11%
        test = {}
        shortest_word = 1001
        out = ''
        for char in licensePlate:
            if char.isalpha():
                test[char.lower()] = test.get(char.lower(), 0) + 1
        for word in words:
            cur = test.copy()
            for char in word:
                if cur.get(char, 0) > 0:
                    cur[char] -= 1
            if not any(list(cur.values())) and len(word) < shortest_word:
                shortest_word = len(word)
                out = word
        return out

    def shortestCompletingWord_best_speed(
            self, licensePlate: str, words: List[str]) -> str:
        a=[i.lower() for i in licensePlate if i.isalpha()]
        b=Counter(a)
        words.sort(key=len)
        for i in words:
            for j in b:
                if i.count(j)<b[j]:
                    break
            else:
                return i

    def shortestCompletingWord_2nd_best(
            self, licensePlate: str, words: List[str]) -> str:
        strs = []
        for char in licensePlate.lower():
            if char.isalpha():
                strs.append(char)
        words.sort(key=len)
        def words_in(strs,words):
            for char in strs:
                if strs.count(char) > words.count(char):
                    return False
            return True
        for word in words:
            if words_in(strs, word):
                return word

    def shortestCompletingWord_3d_best_speed(
            self, licensePlate: str, words: List[str]) -> str:
        d = {}
        l = licensePlate.lower()
        for i in l:
            if ord(i)>=97 and ord(i)<=122:
                d[i] = d.get(i,0)+1
        
        words.sort(key=len)
        for w in words:
            for i,v in d.items():
                if v > w.count(i):
                    break
            else:
                return w
