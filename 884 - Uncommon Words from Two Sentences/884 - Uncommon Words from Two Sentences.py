class Solution:
    def uncommonFromSentences(
            self,
            s1: str,
            s2: str) -> List[str]:  # 11.98% 83.97%
        arr = ' '.join([s1, s2]).split()
        a_map = {}
        for word in arr:
            if word not in a_map:
                a_map[word] = 0
            a_map[word] += 1
        return [key for key, value in a_map.items() if value == 1]

    def uncommonFromSentences_best(self, s1: str, s2: str) -> List[str]:
        res=[]
        listS1, listS2=s1.split(), s2.split()
        countS1S2=Counter(listS1+listS2)
        for word in countS1S2:
            if countS1S2[word]==1:
                res.append(word)
        return res
