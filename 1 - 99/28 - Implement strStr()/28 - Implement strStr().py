class Solution:
    def strStr(self, haystack: str, needle: str) -> int:  # 98.17% 25.15%
        if needle == '':
            return 0
        try:
            return haystack.index(needle)
        except:
            return -1

    def strStr_index(self, haystack, needle):
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)

    def strStr_two(self, haystack: str, needle: str) -> int:  #  95.26% 32.82%
        if needle == '':
            return 0
        for i in range(len(haystack)-len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

    def strStr_study_plan(self, haystack, needle) -> int:  # 98.17% 42.88%
        try:
            return haystack.index(needle)
        except:
            return -1

    def strStr_best_speed(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    def strStr_best_memory(self, haystack: str, needle: str) -> int:
        for i in range(0,len(haystack)-len(needle)+1):
            if needle==haystack[i:len(needle)+i]:
                return i
        return -1
