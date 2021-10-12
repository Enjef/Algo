class Solution(object):
    def removeOuterParentheses(self, s):  # 31.36%  42.37%
        out = ''
        score = 0
        for i in range(len(s)):
            if s[i] == '(' and score == 0:
                score = 1
                continue
            elif s[i] == '(':
                score += 1
            else:
                score -= 1
            if score > 0:
                out += s[i]
        return out

    def removeOuterParentheses_best(self, s):
        count = 0
        results = []
        for char in s:
            if char == "(":
                count += 1
                if count > 1:
                    results.append("(")
            else:
                count -= 1
                if count > 0:
                    results.append(")")
        return "".join(results)
