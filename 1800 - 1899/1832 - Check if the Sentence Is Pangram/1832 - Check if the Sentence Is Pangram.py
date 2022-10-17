class Solution(object):
    # 36%
    def checkIfPangram(self, sentence):
        abc_set = set('abcdefghijklmnopqrstuvwxyz')
        sentence = set(sentence)
        return abc_set == sentence

    # 73.44% 11.66%
    def checkIfPangram_daily(self, sentence: str) -> bool:
        return set(sentence) == set(ascii_lowercase)

    def checkIfPangram_best_speed(self, sentence: str) -> bool:
        l = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
        for i in range(len(l)):
            if l[i] not in sentence:
                return 0
        else:
            return 1

    def checkIfPangram_2nd_best_speed(self, sentence: str) -> bool:
        s = set()
        for c in sentence:
            s.add(c)
        return len(s) == 26

    def checkIfPangram_best_memory(self, sentence: str) -> bool:
        counter = 0
        for c in sentence:
            counter |= (1 << (ord(c) - ord('a')))
        return counter == (1 << 26) - 1

    def checkIfPangram_2d_best_memory(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
