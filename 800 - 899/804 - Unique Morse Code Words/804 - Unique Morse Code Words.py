class Solution(object):
    def uniqueMorseRepresentations(self, words):  # 62.03% 72.18 %
        if len(words) == 1:
            return 1
        m_map = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
        c_map = 'abcdefghijklmnopqrstuvwxyz'
        decode = set()
        for word in words:
            temp = ''
            for char in word:
                temp += m_map[c_map.index(char)]
            decode.add(temp)
        return len(decode)

    def uniqueMorseRepresentations_best(self, words):
        morseCode = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
        letters = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
        res = set()
        for word in words:
            morse = ""
            for letter in word:
                code = morseCode[letters.index(letter)]
                morse = morse+code
            res.add(morse)
        return len(res)
