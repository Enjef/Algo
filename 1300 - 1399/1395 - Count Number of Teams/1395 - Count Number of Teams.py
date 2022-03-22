class Solution:
    def numTeams_TL(self, rating: List[int]) -> int: # Time Limit Exceeded
        out = 0
        n = len(rating)
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if (
                        rating[i] < rating[j] < rating[k] or
                        rating[i] > rating[j] > rating[k]):
                            out += 1
        return out

    def numTeams_v2(self, rating: List[int]) -> int:  # 54.49% 66.56%
        n = len(rating)
        asc = [0] * n
        dsc = [0] * n
        for i in range(n-1):
            for j in range(i+1, n):
                if rating[i] < rating[j]:
                    asc[i] += 1
                else:
                    dsc[i] += 1
        res = 0
        for i in range(n-2):
            for j in range(i+1, n):
                if rating[i] < rating[j]:
                    res += asc[j]
                else:
                    res += dsc[j]
        return res
