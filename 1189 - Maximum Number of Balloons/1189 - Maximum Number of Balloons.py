class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:  # 90.99% 55.38%
        map_b = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        arr = []
        for char in map_b:
            arr.append(text.count(char)//map_b[char])
        return min(arr)

    def maxNumberOfBalloons_best_memory(self, text: str) -> int:
        c = Counter(text)
        mn = float('inf')
        for ch in 'balon':
            if ch == 'l' or ch == 'o':
                mn = min(mn, c[ch] // 2)
            else:
                mn = min(mn, c[ch])
        return mn
