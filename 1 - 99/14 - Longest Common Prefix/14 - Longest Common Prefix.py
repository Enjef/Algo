class Solution:
    def longestCommonPrefix(self, strs) -> str:  # 20.49% 56.69%
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

    def longestCommonPrefix_mock(
            self,
            strs: List[str]) -> str:  # 83.41% 56.69%
        out = ''
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                out += chars[0][0]
            else:
                return out
        return out

    def longestCommonPrefix_best_speed(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        res = ""
        for i in range(len(strs[0])):
            this_char = strs[0][i]
            for word in strs:
                if i > len(word) - 1 or this_char != word[i]:
                    return res
            res += this_char
        return res

    def longestCommonPrefix_best_memory(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i>=len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]
