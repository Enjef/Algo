class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:  # 30.79% 12.62%%
        par = []
        par_ind = []
        for i, char in enumerate(s):
            if par and par[-1] == '(' and char == ')':
                par.pop()
                par_ind.pop()
            elif char in ['(', ')']:
                par.append(char)
                par_ind.append(i)
        out = list(s)
        par_ind = set(par_ind)
        return ''.join(
            [val for i, val in enumerate(out) if i not in par_ind])
