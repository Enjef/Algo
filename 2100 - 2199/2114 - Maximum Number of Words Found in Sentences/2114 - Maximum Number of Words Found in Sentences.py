class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:  # 95.48% 41.30%
        out = 0
        for sentence in sentences:
            out = max(out, len(sentence.split()))
        return out

    def mostWordsFound_best_speed(self, sentences: List[str]) -> int:
        ans=0
        for i in sentences:
            ans = max(ans,len(i.split()))
        return ans

    def mostWordsFound_2nd_best_speed(self, sentences: List[str]) -> int:
        arr = []
        for i in sentences:
            arr.append(len(i.split(' ')))
        return max(arr)
