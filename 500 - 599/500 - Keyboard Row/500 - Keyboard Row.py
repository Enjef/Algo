class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set_1 = set(list("qwertyuiop"))
        set_2 = set(list("asdfghjkl"))
        set_3 = set(list("zxcvbnm"))
        w_map = [set_1, set_2, set_3]
        out = []
        for word in words:
            for row in w_map:
                if not (set(word.lower()) - row):
                    out.append(word)
        return out

    def findWords_better(self, words: List[str]) -> List[str]:
        s1 = set('qwertyuiop')
        s2 = set('asdfghjkl')
        res = []
        s3 = set('zxcvbnm')
        for w in words:
            w1 = w.lower()
            w1 = set(w1)
            if w1 <= s1 or w1 <= s2 or w1 <= s3:
                res.append(w)
        return res
