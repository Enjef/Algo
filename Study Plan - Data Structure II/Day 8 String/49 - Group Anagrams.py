class Solution:
    def groupAnagrams(
            self,
            strs: List[str]) -> List[List[str]]:  # 67.73% 98.28%
        out = {}
        for word in strs:
            cur = ''.join(sorted(word))
            out[cur] = out.get(cur, []) + [word]
        return list(out.values())
