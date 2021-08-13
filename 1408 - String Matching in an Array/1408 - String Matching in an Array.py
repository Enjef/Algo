class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:  # 9.07% 32.08%
        words.sort(key=len)
        out = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    out.append(words[i])
                    break
        return out

    def stringMatching_best_speed(self, words: List[str]) -> List[str]:
        arr = ' '.join(words)
        substr = [i for i in words if arr.count(i) >= 2]
        return substr

    def stringMatching_best_memory(self, words: List[str]) -> List[str]:
        ans=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if i==j:
                    continue
                else:
                    if (words[i] in words[j]) and words[i] not in ans:
                        ans.append(words[i])
        return ans
