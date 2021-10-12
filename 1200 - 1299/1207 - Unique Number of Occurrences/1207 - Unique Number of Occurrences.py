class Solution(object):
    def uniqueOccurrences(self, arr):  # 90.46% 56.89%
        """
        :type arr: List[int]
        :rtype: bool
        """
        x_map = {}
        for num in arr:
            if num not in x_map:
                x_map[num] = 0
            x_map[num] += 1
        return len(x_map) == len(set(x_map.values()))
