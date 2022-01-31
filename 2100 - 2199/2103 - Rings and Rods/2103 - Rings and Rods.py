class Solution:
    def countPoints(self, rings: str) -> int:  # 88.77% 99.14%
        rods = {str(key):set() for key in range(10)}
        for i in range(0, len(rings), 2):
            rods[rings[i+1]].add(rings[i])
        return sum(1 for x in rods.values() if len(x) == 3)

    def countPoints_best_speed(self, s: str) -> int:
        res = 0
        m = defaultdict(lambda : set([]))
        for k in range(0, len(s), 2):
            m[s[k+1]].add(s[k])
        for k, v in m.items():
            res+=(len(v)==3)
        return res

    def countPoints_3rd_best_speed(self, rings: str) -> int:
        X = [set() for i in range(10)]
        for i in range(0,len(rings),2):
            pos = ord(rings[i+1]) - ord('0')
            col = rings[i]
            X[pos].add(col)
        ans  = 0
        for i in X:            
            if len(i) == 3:
                ans+=1
        return ans
