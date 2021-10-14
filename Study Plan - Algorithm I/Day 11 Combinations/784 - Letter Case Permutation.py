class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:  # 7.20% 5.20%
        def helper(st, ind, res=set()):
            if ind == len(st):
                res.add(st)
            for i in range(ind, len(st)):
                if st[i].isalpha:
                    cur = st[:i]+st[i].swapcase()+st[i+1:]
                    if cur not in res:
                        helper(st[:i]+st[i].swapcase()+st[i+1:], i+1, res)
                helper(st, i+1, res)
            return res
        return helper(s, 0)

    def letterCasePermutation_check_in_res(
            self,
            s: str) -> List[str]:  # 36.74% 5.20%
        def helper(st, ind, res=set()):
            if ind == len(st):
                res.add(st)
            for i in range(ind, len(st)):
                if st[i].isalpha:
                    cur = st[:i]+st[i].swapcase()+st[i+1:]
                    if cur not in res:
                        helper(st[:i]+st[i].swapcase()+st[i+1:], i+1, res)
                if st not in res:
                    helper(st, i+1, res)
            return res
        return helper(s, 0)

    def letterCasePermutation_set_iter(
            self,
            s: str) -> List[str]:  # 30.97% 57.95%
        res = set([s])
        for i in range(len(s)):
            for word in res.copy():
                if word[i].isalpha:
                    res.add(word[:i]+word[i].swapcase()+word[i+1:])
        return res
