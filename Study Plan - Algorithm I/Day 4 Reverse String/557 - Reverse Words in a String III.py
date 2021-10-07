class Solution:
    def reverseWords(self, s: str) -> str:  #  35.54% 61.37%
        temp = s.split()
        for i, word in enumerate(temp):
            temp[i] = word[::-1]
        return ' '.join(temp)

    def reverseWords_list_comp(self, s: str) -> str:  # 95.24% 74.97%
        return ' '.join([word[::-1] for word in s.split()])
