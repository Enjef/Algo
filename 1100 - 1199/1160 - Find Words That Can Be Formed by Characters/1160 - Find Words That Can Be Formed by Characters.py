class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def cout_chars(word):
            count_map = {}
            for char in word:
                if char not in count_map:
                    count_map[char] = 1
                else:
                    count_map[char] += 1
            return count_map
        x_map = cout_chars(chars)
        out = ''
        for word in words:
            temp = cout_chars(word)
            append = True
            for val in temp:
                if val not in x_map or val in x_map and temp[val] > x_map[val]:
                    append = False
                    break
            if append:
                out += word
        return len(out)

    def countCharacters_1(
            self,
            words: List[str],
            chars: str) -> int:  # 89.41% 93.20%
        out = ''
        for word in words:
            for char in word:
                append = True
                if word.count(char) > chars.count(char):
                    append = False
                    break
            if append:
                out += word
        return len(out)

    def countCharacters_mock(
            self,
            words: List[str],
            chars: str) -> int:  # 78.76% 26.73%
        out = 0
        chars_count = {}
        for char in chars:
            chars_count[char] = chars_count.get(char, 0) + 1
        for word in words:
            for char in set(word):
                if (
                        char not in chars_count or
                        word.count(char) > chars_count.get(char)):
                    break
            else:
                out += len(word)
        return out
