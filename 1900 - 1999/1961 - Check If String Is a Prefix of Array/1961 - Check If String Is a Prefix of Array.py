class Solution:
    def isPrefixString(self, s: str, words: List[str]):  # 49.50% 98.32%
        n = len(s)
        cur = 0
        for i, word in enumerate(words):
            cur += len(word)
            if cur >= n:
                return s == ''.join(words[:i+1])
        return False

    def isPrefixString_best_speed(self, s: str, words: List[str]) -> bool:
        len_str = len(s)
        total = 0
        ss = ''
        for i in words:
            total += len(i)
            ss += i
            if total >= len_str:
                break
        if ss == s:
            return True
        else:
            return False

    def isPrefixString_2nd_best_speed(self, s: str, words: List[str]) -> bool:
        news = ''
        for word in words:
            news += word
            if news == s:
                return True
        return False
