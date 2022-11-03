class Solution:
    # 48.75% 12.75% (72.53% 54.38%)
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        count = Counter(words)
        odd_same = 0
        seen = set()
        for key, val in count.items():
            if key in seen:
                continue
            second = key[::-1]
            if key == second:
                if val % 2:
                    odd_same = 1
                res += val//2
                continue
            if second in count:
                res += min(val, count[second])
            seen.add(second)
        return 4 * res + 2 * int(odd_same == 1)


class Solution_best_speed:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)

        def search(s, counter):
            ans = len(s)
            for w, count in counter.items():
                if count == 0:
                    continue
                if (w != w[::-1] and counter.get(w[::-1], 0) > 0) or \
                        (w == w[::-1] and counter.get(w[::-1], 0) > 1):
                    s = f'{w}{s}{w[::-1]}'
                    counter[w] -= 1
                    counter[w[::-1]] -= 1
                    ans = max(search(s, counter), ans)
                    s = s[2:-3]
                    counter[w] += 1
                    counter[w[::-1]] += 1
            return ans

        ans = 0
        hasDouble = False
        dist_words = list(counter.keys())
        for w in dist_words:
            count = counter.pop(w, 0)
            if not count:
                continue
            if w[0] != w[-1]:
                pair_count = counter.pop(w[::-1], 0)
                ans += 2*min(count, pair_count)
            else:
                if not hasDouble:
                    ans += count
                    hasDouble = 2*(count//2) != count
                else:
                    ans += 2*(count//2)
        return ans*2


class Solution_best_memory:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)
        ans = 0
        odd = 0
        seen = set()
        for word, cnt in counter.most_common():
            if word in seen:
                continue
            seen.add(word)
            if word[0] == word[1] and cnt % 2 == 0:
                ans += 2 * counter[word]
                continue
            if word[0] == word[1] and odd == 0:
                odd = 2 * counter[word]
                continue
            if word[0] == word[1]:
                ans += 4 * (counter[word] // 2)
                continue
            if word[0] != word[1] and word[::-1] in counter:
                ans += 4 * min(counter[word], counter[word[::-1]])
                seen.add(word[::-1])
        return ans + odd
