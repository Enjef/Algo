class Solution:
    # 32.60% 66.02% (96.56% 66.02%)
    def rearrangeCharacters(self, s: str, target: str) -> int:
        storage = Counter(s)
        tar = Counter(target)
        result = len(s)
        for char in tar:
            result = min(result, storage[char]//tar[char])
        return result
