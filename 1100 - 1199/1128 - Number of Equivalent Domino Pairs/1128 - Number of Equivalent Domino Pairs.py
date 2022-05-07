class Solution:
    def numEquivDominoPairs(
            self, dominoes: List[List[int]]) -> int:  # 94.24% 29.55%
        counter = defaultdict(int)
        total = 0
        for el in dominoes:
            cur = tuple(sorted(el))
            if cur in counter:
                total += counter[cur]
            counter[cur] += 1
        return total

    def numEquivDominoPairs_best_speed(self, dominoes: List[List[int]]) -> int:
        return sum(list(map(lambda x: math.comb(x, 2) if x > 1 else 0, collections.Counter(list(map(lambda x: tuple(sorted(x)), dominoes))).values())))

    def numEquivDominoPairs_2nd_best_speed(self, dominoes):
        count_dict = defaultdict(int)
        for dom in dominoes:
            count_dict[tuple(sorted(dom))] += 1
        pairs = 0
        for dom, count in count_dict.items():
            if count > 1:
                pairs += count*(count-1)//2
        return pairs

    def numEquivDominoPairs_best_memory(self, dominoes: List[List[int]]) -> int:
        for dum in dominoes:
            dum.sort()
        cnt = 0
        mapu = defaultdict(int)
        while dominoes:
            tile = dominoes.pop(0)
            tiler = copy.deepcopy(tile)
            tiler.reverse()
            if tile in dominoes:
                mapu[str(tile)] += 1
        cnt = 0
        for i in mapu:
            if mapu[i] > 0:
                cnt += (1+mapu[i])*(mapu[i]/2)

        return int(cnt)
