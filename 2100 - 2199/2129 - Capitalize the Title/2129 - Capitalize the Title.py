class Solution:
    def capitalizeTitle(self, title: str) -> str:  # 87.24% 94.80%
        return ' '.join(
            word.capitalize() if len(word)>2 else word
            for word in title.lower().split()
        )