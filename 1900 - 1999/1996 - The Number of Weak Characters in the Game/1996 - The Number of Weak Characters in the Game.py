class Solution:
    # 5.04% 49.26%
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort()
        n = len(properties)
        arr = [float('-inf')] * n
        cur = float('-inf')
        for i in range(n-1, -1, -1):
            cur = max(cur, properties[i][1])
            arr[i] = cur
        out = 0
        for x, y in properties:
            left, right = 0, n-1
            while left < right:
                mid = (left+right)//2
                if properties[mid][0] > x:
                    right = mid
                else:
                    left = mid + 1
            if properties[right][0] > x and arr[right] > y:
                out += 1
        return out

    # 5.04% 87.07%
    def numberOfWeakCharacters_v2(self, properties: List[List[int]]) -> int:
        properties.sort()
        n = len(properties)
        properties[-1].append(properties[-1][1])
        for i in range(n-2, -1, -1):
            properties[i].append(max(properties[i][1], properties[i+1][2]))
        out = 0
        for x, y, _ in properties:
            left, right = 0, n-1
            while left < right:
                mid = (left+right)//2
                if properties[mid][0] > x:
                    right = mid
                else:
                    left = mid + 1
            if properties[right][0] > x and properties[right][2] > y:
                out += 1
        return out

    def numberOfWeakCharacters_best_speed(self, properties: List[List[int]]) -> int:
        max_defense_for_attacks = [0] * int(1e5 + 2)
        max_att = 0
        for att, defense in properties:
            if defense > max_defense_for_attacks[att]:
                max_defense_for_attacks[att] = defense
            if att > max_att:
                max_att = att
        current_max = 0
        for i in range(max_att, 0, -1):
            current_max = max(current_max, max_defense_for_attacks[i])
            max_defense_for_attacks[i] = current_max
        result = 0
        for att, defense in properties:
            if defense < max_defense_for_attacks[att + 1]:
                result += 1
        return result

    def numberOfWeakCharacters_2nd_best_speed(self, properties: List[List[int]]) -> int:
        max_attack = max(attack for attack, defence in properties)
        defence_list = [0] * (max_attack + 2)
        for attack, defence in properties:
            defence_list[attack] = max(defence_list[attack], defence)
        for i in range(max_attack, -1, -1):
            defence_list[i] = max(defence_list[i], defence_list[i + 1])
        res = 0
        for attack, defence in properties:
            if defence_list[attack + 1] > defence:
                res += 1
        return res

    def numberOfWeakCharacters_best_memory(self, p: List[List[int]]) -> int:
        p.sort()
        smallest_a, max_d = p.pop()
        rt = 0
        while p:
            a, d = p.pop()
            if a == smallest_a:
                continue
            if d < max_d:
                rt += 1
            elif d > max_d:
                while p:
                    a_a, d_d = p.pop()
                    if a_a == a:
                        if d_d < max_d:
                            rt += 1
                    else:
                        p.append([a_a, d_d])
                        break
                max_d = d
                smallest_a = a
        return rt

    def numberOfWeakCharacters_2nd_best_memory(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        currmax = 0
        ans = 0
        for attack, defense in properties:
            if defense < currmax:
                ans += 1
            else:
                currmax = defense
        return ans

    def numberOfWeakCharacters_3d_best_memory(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        prev, res = -1, 0
        for a, d in properties:
            if d < prev:
                res += 1
            prev = max(prev, d)
        return res
