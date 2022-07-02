class Solution:
    # 20.88% 34.98%
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        h_max = 0
        v_max = 0
        for i in range(1, len(horizontalCuts)):
            h_max = max(h_max, horizontalCuts[i]-horizontalCuts[i-1])
        for i in range(1, len(verticalCuts)):
            v_max = max(v_max, verticalCuts[i]-verticalCuts[i-1])
        return h_max * v_max % (10**9+7)

        # 30.04% 94.22%
    def maxArea_v2(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        h_max = max(horizontalCuts[0], h-horizontalCuts[-1])
        v_max = max(verticalCuts[0], w-verticalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            h_max = max(h_max, horizontalCuts[i]-horizontalCuts[i-1])
        for i in range(1, len(verticalCuts)):
            v_max = max(v_max, verticalCuts[i]-verticalCuts[i-1])
        return h_max * v_max % (10**9+7)

    def maxArea_best_speed(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        m1 = 1
        m2 = 1
        h1 = [0]+horizontalCuts+[h]
        h2 = [0]+verticalCuts+[w]
        h1 = list(sorted(h1))
        h2 = list(sorted(h2))
        for i in range(len(h1)-1):
            if h1[i+1]-h1[i] > m1:
                m1 = h1[i+1]-h1[i]
        for i in range(len(h2)-1):
            if h2[i+1]-h2[i] > m2:
                m2 = h2[i+1]-h2[i]
        return (m1*m2) % (1000000000+7)

    def maxArea_best_memory(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        horizontalCuts.sort()
        maxhgap = max(horizontalCuts[i]-horizontalCuts[i-1] for i in range(1, len(horizontalCuts)))
        verticalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.sort()
        maxvgap = max(verticalCuts[i]-verticalCuts[i-1] for i in range(1, len(verticalCuts)))
        print(maxvgap)
        return (maxhgap * maxvgap)% (10 ** 9 + 7)
