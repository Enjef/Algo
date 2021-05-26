class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        i = 0
        while i <= len(version1) - 1 and i <= len(version2) - 1:
            if int(version1[i]) < int(version2[i]):
                return -1
            elif int(version1[i]) > int(version2[i]):
                return 1
            else:
                i += 1
        if len(version1) == len(version2):
            return 0
        if len(version1) > len(version2):
            if False in [int(x) == 0 for x in version1[i:]]:
                return 1
            else:
                return 0
        else:
            if False in [int(x) == 0 for x in version2[i:]]:
                return -1
            else:
                return 0
