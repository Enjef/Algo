class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        mapx = {}
        difference = set(list1) - set(list2)
        for i in range(len(list1)):
            if list1[i] not in difference:
                mapx[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in mapx:
                mapx[list2[i]] += i
        keys = mapx.keys()
        vals = mapx.values()
        index_list = [i for i, x in enumerate(vals) if x == min(vals)]
        return [keys[i] for i in index_list]

    def findRestaurant_best(self, list1, list2):
        d = {}
        for i, x in enumerate(list1):
            d[x] = i
        m = float('inf')
        res = []
        for i, x in enumerate(list2):
            if x in d:
                if i + d[x] < m:
                    m = i+d[x]
                    res = [x]
                elif i+d[x] == m:
                    res.append(x)
        return res
