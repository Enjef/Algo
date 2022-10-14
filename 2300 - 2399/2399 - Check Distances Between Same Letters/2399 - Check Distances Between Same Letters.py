class Solution:
    # 76.19% 20.78% (17.74% 20.78%)
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        coords = defaultdict(list)
        for i, char in enumerate(s):
            coords[ord(char)-ord('a')].append(i)

        for char, (first, second) in coords.items():
            if distance[char] != second - first - 1:
                return False
        return True

    def checkDistances_best_speed(self, s: str, distance: List[int]) -> bool:
        for i, dist in enumerate(distance):
            target = chr(97+i)
            value1 = s.find(target)
            value2 = s.rfind(target)
            if value2 - value1 - 1 != dist and value2 - value1 != 0:
                return False
        return True

    def checkDistances_2nd_best_speed(self, s: str, distance: List[int]) -> bool:
        d = {}
        for i, c in enumerate(s):
            if c not in d:
                d[c] = i
            else:
                if i - d[c] - 1 != distance[ord(c) - ord('a')]:
                    return False
        return True
