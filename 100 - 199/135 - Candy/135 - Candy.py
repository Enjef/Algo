class Solution:
    # 38.56% 74.92%
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        out = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                out[i] = max(out[i-1] + 1, out[i])
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                out[i] = max(out[i+1] + 1, out[i])
        return sum(out)

    def candy_best_speed(self, ratings: List[int]) -> int:
        if len(ratings) == 0:
            return 0
        pre = maxPre = 1
        sequence = 0
        result = 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                sequence = 0
                pre += 1
                maxPre = pre
                result += pre
            elif ratings[i] < ratings[i-1]:
                sequence += 1
                result = result + sequence
                if sequence >= maxPre:
                    result += 1
                pre = 1
            else:
                result += 1
                sequence = 0
                pre = maxPre = 1
        return result
