class Solution:
    def distributeCandies(
            self,
            candies: int,
            num_people: int) -> List[int]:  # 5.38% 93.89%
        out = [0]*num_people
        cur = 1
        while candies:
            for i in range(num_people):
                if cur > candies:
                    out[i] += candies
                    candies = 0
                    break
                out[i] += cur
                candies -= cur
                cur += 1
        return out

    def distributeCandies_second_to_best_speed(
            self,
            candies: int,
            num_people: int) -> List[int]:  # 68.46% 53.06%
        res = [0] * num_people
        cur = 1
        i = 0
        while candies:
            if candies >= cur:
                candies -= cur
                res[i] += cur
                cur += 1
                i += 1
                if i == num_people:
                    i = 0
            else:
                res[i] += candies
                candies = 0
        return res

    def distributeCandies_best_memory(
            self,
            candies: int,
            num_people: int) -> List[int]:  # 68.46% 80.20%
        result = [0] * num_people
        n = 1
        while candies > 0:
            if candies <= n:
                result[(n-1) % num_people] += candies
            else:
                result[(n-1) % num_people] += n
            candies -= n
            n += 1
        return result
