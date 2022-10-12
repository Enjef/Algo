class Solution:
    # 33.43% 67.60% (43.73% 29.64%)
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        n, m = len(players), len(trainers)
        i, j = n-1, m-1
        res = 0
        while i > -1 and j > -1:
            if players[i] <= trainers[j]:
                res += 1
                i -= 1
                j -= 1
            else:
                i -= 1
        return res

    def matchPlayersAndTrainers_best_speed(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort()
        players.sort(reverse=True)
        ans = 0
        for trainer in trainers:
            if players and players[-1] <= trainer:
                ans += 1
                players.pop()
        return ans

    def matchPlayersAndTrainers_2nd_best_speed(self, players: List[int], trainers: List[int]) -> int:
        players = sorted(players)
        trainers = sorted(trainers)
        i = 0
        res = 0
        l = len(trainers)
        for p in players:
            while i < l and trainers[i] < p:
                i += 1
            if i == l:
                return res
            res += 1
            i += 1
        return res

    def matchPlayersAndTrainers_best_memory(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        count = 0
        for player in players:
            for trainer in trainers:
                if player <= trainer:
                    count += 1
                    trainers.remove(trainer)
                    break
        return count
