class Solution:
    def arrangeWords(self, text: str) -> str:  # 46.92% 66.78%
        text = text.lower()
        s = sorted(text.split(), key=len)
        s[0] = ''.join([s[0][0].upper(), s[0][1:]])
        return ' '.join(s)

    def arrangeWords_v2(self, text: str) -> str:  # 69.86% 81.85%
        s = ' '.join(sorted(text.lower().split(), key=len))
        return ''.join([s[0].upper(), s[1:]])

    def arrangeWords_best_speed(self, text: str) -> str:
        text = text.lower().split(' ')
        text.sort(key=len)
        text = " ".join(text)
        text[0].upper()
        return text[0].upper() + text[1::]

    def arrangeWords_2nd_best_speed(self, text: str) -> str:
        return ' '.join(sorted(text.split(), key = len)).capitalize()
