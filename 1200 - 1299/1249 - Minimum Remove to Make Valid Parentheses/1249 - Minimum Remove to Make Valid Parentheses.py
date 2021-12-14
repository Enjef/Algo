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

    def minRemoveToMakeValid_best_speed(self, s: str) -> str:
        s,stack = list(s), []
        for i,element in enumerate(s):
            if element == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
            elif element == '(':
                stack.append(i)
        while stack:
            i = stack.pop()
            s[i] = ''
        return ''.join(s)

    def minRemoveToMakeValid_2nd_best_speed(self, s: str) -> str:
        s_list = list(s)
        count = 0
        for index in range(len(s_list)):
            if s_list[index] == "(":
                count += 1
            elif s_list[index] == ")":
                count -= 1
            else:
                continue 
            if count < 0:
                s_list[index] = ""
                count += 1
        for index in reversed(range(len(s_list))):
            if count <= 0:
                break
            if s_list[index] == "(":
                s_list[index] = ""
                count -= 1
        return "".join(s_list)

    def minRemoveToMakeValid_best_memory(self, s: str) -> str:
        if s is None:
            return s
        para = []
        paraDict = {}
        for i in range(len(s)):
            if para and para[-1]  == '(' and s[i] == ')':
                para.pop()
                paraDict.popitem()
            else:
                if s[i] == ')' or s[i] == '(':
                    paraDict[i] = s[i]
                    para.append(s[i])
        c = 0
        returnStr = s
        for key in paraDict:
            returnStr = returnStr[:key-c] + returnStr[key+1-c:]
            c += 1
        return returnStr
