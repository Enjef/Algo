class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:  # 77.46% 7.13%
        ind = {num: i for i, num in enumerate(score)}
        out = [0] * len(score)
        arr = [-x for x in score]
        heapify(arr)
        places = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        n = min(len(score), 3)
        for i in range(n):
            out[ind[-heappop(arr)]] = places[i]
        j = 4
        while arr:
            out[ind[-heappop(arr)]] = str(j)
            j += 1
        return out + arr

    def findRelativeRanks_v2(self, score):  # 56.15% 23.03%
        arr = [(x, i) for i, x in enumerate(score)]
        arr.sort(reverse=True)
        places = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        n = min(len(score), 3)
        for i in range(n):
            score[arr[i][1]] = places[i]
        for j in range(i+1, len(arr)):
            score[arr[j][1]] = str(j+1)
        return score

    def findRelativeRanks_best_speed(self, score: List[int]) -> List[str]:
        sort_score = score.copy()
        lookup = {k: v for v, k in enumerate(score)}
        sort_score.sort(reverse=True)
        for i in range(len(sort_score)):
            if i > 2:
                score[lookup[sort_score[i]]] = str(i+1)
            elif i == 0:
                score[lookup[sort_score[i]]] = 'Gold Medal'
            elif i == 1:
                score[lookup[sort_score[i]]] = 'Silver Medal'
            elif i == 2:
                score[lookup[sort_score[i]]] = 'Bronze Medal'
        return score

    def findRelativeRanks_3d_best_speed(self, score: List[int]) -> List[str]:
        rank = ['Gold Medal', 'Silver Medal', 'Bronze Medal'] + \
            [str(i) for i in range(4, len(score) + 1)]
        idxs = {n: i for i, n in enumerate(sorted(score, reverse=True))}
        return [rank[idxs[n]] for n in score]

    def findRelativeRanks_best_memory(self, score: List[int]) -> List[str]:
        k = sorted(score)
        if len(k) == 1:
            score[score.index(k[-1])] = 'Gold Medal'
            return score
        if len(k) == 2:
            score[score.index(k[-1])] = 'Gold Medal'
            score[score.index(k[-2])] = 'Silver Medal'
            return score
        if len(k) == 3:
            score[score.index(k[-1])] = 'Gold Medal'
            score[score.index(k[-2])] = 'Silver Medal'
            score[score.index(k[-3])] = 'Bronze Medal'
            return score
        score[score.index(k[-1])] = 'Gold Medal'
        score[score.index(k[-2])] = 'Silver Medal'
        score[score.index(k[-3])] = 'Bronze Medal'
        co = 4
        for j in range(len(k)-3):
            score[score.index(k[-1*co])] = str(co)
            co += 1
        return score

    def findRelativeRanks_2nd_best_memory(self, score: List[int]) -> List[str]:
        x = score[:]
        score.sort(reverse=True)
        for i, num in enumerate(x):
            if score.index(num) == 0:
                x[i] = 'Gold Medal'
            elif score.index(num) == 1:
                print(num, score.index(num), i)
                x[i] = 'Silver Medal'
            elif score.index(num) == 2:
                x[i] = 'Bronze Medal'
            else:
                x[i] = str(score.index(num) + 1)
        return x
