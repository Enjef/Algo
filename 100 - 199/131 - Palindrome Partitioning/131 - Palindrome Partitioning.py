class Solution:
    # 14.61% 78.11% (31.19% 78.36%)
    def partition(self, s: str) -> List[List[str]]:
        def helper(cur, way, res):
            if not cur:
                res.add(tuple(way))
                return
            for i in range(n+1):
                if cur[:i+1] == cur[:i+1][::-1]:
                    helper(cur[i+1:], way+[cur[:i+1]], res)
            return

        res = set()
        n = len(s)
        helper(s, [], res)
        return res


class Solution_best_speed:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(start, end) -> bool:
            if start >= end:
                return True
            if palindrome[start][end] is None:
                palindrome[start][end] = s[start] == s[end] and is_palindrome(
                    start + 1, end - 1)
            return palindrome[start][end]

        N = len(s)
        palindrome: List[List[Optional[bool]]] = [[None] * N for _ in range(N)]
        partition_from = [[] for _ in range(N)]

        for start in reversed(range(N)):
            for end in range(start, N):
                if is_palindrome(start, end):
                    if end == N - 1:
                        partition_from[start].append([s[start: end + 1]])
                    else:
                        partition_from[start] += [
                            [s[start: end + 1]] +
                            partition for partition in partition_from[end + 1]
                        ]
        return partition_from[0]


class Solution_2nd_speed:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            stack = []
            for char in s[:ceil(len(s) / 2)]:
                stack.append(char)
            for char in s[len(s) // 2:]:
                if char != stack.pop():
                    return False
            return True

        def getNewPalindromes(ending: int):
            res = []
            for i in range(ending, 0, -1):
                sub = s[i-1:ending]
                if isPalindrome(sub):
                    res.append(sub)
            return res

        res = [[[]]]
        for i in range(1, len(s)+1):
            new = getNewPalindromes(i)
            res.append([])
            for currNew in new:
                oldIndex = len(res) - len(currNew) - 1
                prev = res[oldIndex]
                prev = list(map(lambda x: x + [currNew], prev))
                res[-1] += prev
        return res[-1]


# 97.37% 5.29%
class Solution_discussion:
    @cache
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                for suf in self.partition(s[i:]):
                    ans.append([s[:i]] + suf)
        return ans


class Solution_best_memory:
    ans = []

    def partition(self, s: str) -> List[List[str]]:
        self.ans.clear()

        def is_palindrome(word):
            front, back = 0, len(word) - 1
            while front < back:
                if word[front] != word[back]:
                    return False
                front += 1
                back -= 1
            return True

        def backtrack(word, cur=[], w=[], ind=0):
            if ind >= len(word):
                self.ans.append(cur.copy())
                return
            for i in range(ind, len(word)):
                w.append(word[i])
                if is_palindrome(w):
                    cur.append(''.join(w))
                    backtrack(word, cur, [], i + 1)
                    cur.pop()

        backtrack(s)
        return self.ans
