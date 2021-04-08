class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ''
        out = strs[0]
        for word in range(1, len(strs)):
            j = 0
            while j <= len(strs[word])-1 and j <= len(out)-1:
                if out[j] == strs[word][j]:
                    j += 1
                    if len(strs[word]) == j and word == len(strs)-1:
                        return strs[word]
                    continue
                if len(out) == 1:
                    return ''
                out = out[:j]
                break
            if len(out) > len(strs[word]):
                out = strs[word]
        return out


x = Solution()
print(x.longestCommonPrefix(["aaa","aa","aaa"]))
