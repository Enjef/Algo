class Solution:
    def countValidWords(self, sentence: str) -> int:  # 46.51% 58.80%
        def tester(word):
            if word.isdigit():
                return 0
            chars = 0
            hyphen = 0
            digits = 0
            for i, char in enumerate(word):
                if char.isdigit():
                    digits += 1
                if char.isalpha():
                    chars += 1
                if char in ',.!' and i < len(word)-1:
                    return 0
                if char is '-':
                    hyphen += 1
                    if (
                        hyphen > 1 or not chars or
                        i == len(word)-1 or not word[i+1].isalpha()
                    ):
                        return 0
                if digits and chars:
                    return 0
            return int(chars > 0 or word in ',.!')
        out = 0
        for el in sentence.split():
            out += tester(el)
        return out

    def countValidWords_best_speed(self, sentence: str) -> int:
        res = 0
        for word in sentence.split():
            count_hype = 0
            for i, ch in enumerate(word):
                if ch.isdigit():
                    break
                if ch in ["!", ".", ","]:
                    if i < len(word) - 1:
                        break
                    continue
                if ch.islower():
                    continue
                count_hype += 1
                if count_hype > 1:
                    break
                if (
                        i == 0 or i == len(word) - 1 or
                        not word[i-1].islower() or
                        not word[i+1].islower()):
                    break
            else:
                res += 1
        return res

    def countValidWords_best_memory(self, sentence: str) -> int:
        ans = 0
        for word in sentence.split():
            if word.strip() and re.fullmatch('^([a-z]+(-?[a-z]+)?)?[\.,!]?$', word.strip()):
                ans += 1
        return ans

    def countValidWords_2nd_best_memory(self, sentence: str) -> int:
        res = 0
        for word in sentence.split():
            hyphen, punc = 0, 0
            for i, c in enumerate(word):
                if c.isdigit():
                    break
                if c == '-':
                    if (
                        i == 0 or i == len(word)-1 or
                        not (word[i-1].isalpha() and word[i+1].isalpha())
                    ):
                            break
                    hyphen += 1
                if c in ['!', ',', '.']:
                    if i != len(word)-1:
                        break
                    punc += 1
                if hyphen > 1 or punc > 1:
                    break
            else:
                res += 1
        return res
