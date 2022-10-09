class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref) == 1:
            return pref
        cur = pref[0]
        for i in range(1, len(pref)):
            pref[i] ^= cur
            cur ^= pref[i]
        return pref

    def findArray_v2(self, pref: List[int]) -> List[int]:
        cur = 0
        for i in range(len(pref)):
            pref[i] ^= cur
            cur ^= pref[i]
        return pref

    def findArray_v3(self, pref: List[int]) -> List[int]:
        return [pref[0]] + [pref[i-1] ^ pref[i] for i in range(1, len(pref))]

    def findArray_best_speed(self, pref: List[int]) -> List[int]:
        ans = []
        for i, x in enumerate(pref):
            if i == 0:
                ans.append(x)
            else:
                ans.append(x ^ pref[i-1])
        return ans

    def findArray_2nd_best_speed(self, pref: List[int]) -> List[int]:
        ans = []
        p = 0
        for x in pref:
            ans.append(x ^ p)
            p ^= ans[-1]
        return ans

    def findArray_best_memory(self, pref: List[int]) -> List[int]:
        x = 0
        for i in range(len(pref)):
            yield x ^ pref[i]
            x = pref[i]
