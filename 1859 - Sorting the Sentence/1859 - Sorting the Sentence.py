class Solution:
    def sortSentence(self, s) -> str: #  85.66% 14.43%
        out = [''] * 9
        s = s.split()
        for i in s:
            out[int(i[-1])-1] = i[:-1]
        out = [x for x in out if x != '']
        return ' '.join(out)

    def sortSentence_better(self, s: str) -> str: #  85.66% 91.97%
        arr = s.split(' ')
        ret = [''] * len(arr)
        for i in arr:
            ret[int(i[-1])-1] = i[:-1]
        return ' '.join(ret)
