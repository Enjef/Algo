from typing import List


class Solution:
    # 16.03% 5.04% (17.49% 5.04%)
    def maxLength(self, arr: List[str]) -> int:
        res = 0
        unique = set()
        for el in arr:
            n = len(el)
            if n == len(set(el)):
                unique.add(el)
                res = max(res, n)

        els = list(unique)
        n = len(els)
        for first in els:
            new = set()
            for second in unique:
                cur = second+first
                m = len(cur)
                if m == len(set(cur)):
                    new.add(cur)
                    res = max(res, m)
            unique |= new
        return res

    # 62.08% 5.04%
    def maxLength_v2_discussion(self, arr: List[str]) -> int:
        unique = [set()]
        for first in arr:
            if len(first) != len(set(first)):
                continue
            first = set(first)
            for second in unique[:]:
                if not first & second:
                    cur = first | second
                    unique.append(cur)
        return max(len(x) for x in unique)


class Solution_best_speed:
    def maxLength_1st(self, arr: List[str]) -> int:
        def bit_mask(word):
            out = 0
            for c in word:
                out |= (1 << (ord(c) - ord('a')))
            return out

        arr = [(bit_mask(x), len(x)) for x in arr if len(set(x)) == len(x)]
        queue = [(0, 0)]
        out = 0
        for word_mask, word_len in arr:
            old_queue = queue.copy()
            for subseq_len, subseq_mask in old_queue:
                if word_mask & subseq_mask == 0:
                    queue.append(
                        (subseq_len + word_len, word_mask | subseq_mask))
                    out = max(out, queue[-1][0])
        return out

    def maxLength_3d(self, arr: List[str]) -> int:
        def max_len_of_merged_word(words):
            largest, M = 0, len(words)
            for i in range(M):
                word_set_1 = set(words[i])
                size = len(words[i])
                for j in range(M):
                    if j == i:
                        continue
                    word_set_2 = set(words[j])
                    if word_set_1.isdisjoint(word_set_2):
                        size += len(words[j])
                        word_set_1 = word_set_1.union(word_set_2)
                largest = max(largest, size)
            return largest

        strs = [arr[i]
                for i in range(len(arr)) if len(arr[i]) == len(set(arr[i]))]
        return max(
            max_len_of_merged_word(strs),
            max_len_of_merged_word(sorted(strs, reverse=True)))


class Solution_best_memory:
    def maxLength_1st(self, arr: List[str]) -> int:
        new_arr = [set(x) for x in arr if len(x) == len(set(x))]
        n = len(new_arr)

        def solve(i, s):
            if i == n:
                self.res = max(self.res, len(s))
                return
            if len(s & new_arr[i]) == 0:
                solve(i+1, s | new_arr[i])
                solve(i+1, s)
            else:
                solve(i+1, s)

        self.res = 0
        solve(0, set())
        return self.res

    def maxLength_2nd(self, arr: List[str]) -> int:

        def helper(current, i):
            if i >= len(arr):
                return len(current)
            if len(set(arr[i])) != len(arr[i]):
                return helper(current, i + 1)
            for c in arr[i]:
                if c in current:
                    return helper(current, i + 1)
            return max(helper(current + arr[i], i + 1), helper(current, i + 1))

        return helper('', 0)

    def maxLength_3d(self, arr: List[str]) -> int:
        M = 0
        n = len(arr)

        def is_unique(s):
            return len(s) == len(set(s))

        def dfs(start, curr):
            nonlocal M
            if is_unique(curr):
                M = max(M, len(curr))
            else:
                return
            for i in range(start, n):
                dfs(i + 1, curr + arr[i])

        dfs(0, '')
        return M
