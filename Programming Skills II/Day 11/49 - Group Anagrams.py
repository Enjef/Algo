class Solution:
    def groupAnagrams(self, strs):  # 96.33% 34.60%
        words = defaultdict(list)
        for word in strs:
            words[tuple(sorted(word))].append(word)
        return words.values()
