class Solution:
    # 10.80% 30.80% (5.2% 73.64%)
    def removeAnagrams(self, words: List[str]) -> List[str]:
        new = [words[0]]
        for i in range(1, len(words)):
            if Counter(words[i]) != Counter(words[i-1]):
                new.append(words[i])
        return new

    # 61.92% 73.64%
    def removeAnagrams_v2(self, words: List[str]) -> List[str]:
        prev = sorted(words[0])
        new = [words[0]]
        for word in words[1:]:
            cur = sorted(word)
            if cur != prev:
                new.append(word)
            prev = cur
        return new

    # 18.83% 30.80%
    def removeAnagrams_v3(self, words: List[str]) -> List[str]:
        prev = Counter(words[0])
        new = [words[0]]
        for word in words[1:]:
            cur = Counter(word)
            if cur != prev:
                new.append(word)
            prev = cur
        return new


class Solution_best_speed:
    def removeAnagrams_1st(self, words: List[str]) -> List[str]:
        i = 1
        while i < len(words):
            if sorted(words[i - 1]) == sorted(words[i]):
                words.pop(i)
            else:
                i += 1
        return words

    def removeAnagrams_2nd(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return words
        rear, front = 0, 1
        while front < len(words):
            if sorted(words[front]) == sorted(words[rear]):
                words.pop(front)
            else:
                rear, front = rear+1, front+1
        return words

    def removeAnagrams_3d(self, words: List[str]) -> List[str]:
        i = 0
        while i < len(words) - 1:
            if sorted(words[i]) == sorted(words[i + 1]):
                words.remove(words[i + 1])
                continue
            i += 1
        return words
