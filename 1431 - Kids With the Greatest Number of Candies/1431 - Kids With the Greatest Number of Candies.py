class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        out = [False] * len(candies)
        max_el = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_el:
                out[i] = True
        return out
