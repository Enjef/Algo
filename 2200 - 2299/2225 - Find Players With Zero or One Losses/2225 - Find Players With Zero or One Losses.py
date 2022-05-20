class Solution:
    def findWinners(
            self, matches: List[List[int]]) -> List[List[int]]:  # 23.23% 50.93%
        counter = defaultdict(int)
        for winner, loser in matches:
            if winner not in counter:
                counter[winner]
            counter[loser] += 1
        answer = [[], []]
        for player in sorted(counter):
            if not counter[player]:
                answer[0].append(player)
            if counter[player] == 1:
                answer[1].append(player)
        return answer
        
    def findWinners_v2(
            self, matches: List[List[int]]) -> List[List[int]]:  # 82.35% 67.99%
        counter = dict()
        for winner, loser in matches:
            if winner not in counter:
                counter[winner] = 0
            counter[loser] = counter.get(loser, 0) + 1
        answer = [[], []]
        for player in sorted(counter):
            if not counter[player]:
                answer[0].append(player)
            if counter[player] == 1:
                answer[1].append(player)
        return answer

    def findWinners_best_speed(self, matches: List[List[int]]) -> List[List[int]]:
        winStreak, lostOnce, lostMore = set(), set(), set()
        for w, l in matches:
            if w not in lostOnce and w not in lostMore and w not in winStreak:
                winStreak.add(w)
            if l in lostOnce:
                lostOnce.remove(l)
                lostMore.add(l)
            elif l not in lostMore:
                lostOnce.add(l)
                if l in winStreak:
                    winStreak.remove(l)
        return [sorted(list(winStreak)), sorted(list(lostOnce))]
            
    def findWinners_best_memory(
            self, matches: List[List[int]]) -> List[List[int]]:
        d_lose = defaultdict(int)
        d_win = defaultdict(int)
        for w, l in matches:
            d_win[w] = 1
            d_lose[l] += 1
        res_0 = []
        for k, v in d_lose.items():
            if v == 1:
                res_0.append(k)
            if k in d_win:
                del d_win[k]
        res_1 = sorted(d_win.keys())
        res_0.sort()
        return [res_1, res_0]
           