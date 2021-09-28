class Solution:
    def letterCombinations(self, digits: str) -> List[str]:  # 67.90% 61.59%
        if not digits:
            return []
        table = [
            'abc', 'def',
            'ghi', 'jkl', 'mno',
            'pqrs', 'tuv', 'wxyz',
        ]
        if len(digits) == 1:
            return list(table[int(digits)-2])
        out = ['']
        while digits:
            cur = digits[0]
            digits = digits[1:]
            temp = []
            for char in table[int(cur)-2]:
                for base in out:
                    temp.append(base + char)
            out = temp
        return out
