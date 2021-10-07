class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        for i, word in enumerate(temp):
            temp[i] = word[::-1]
        return ' '.join(temp)

    def reverseWords_list_comp(self, s: str) -> str:
        return ' '.join([word[::-1] for word in s.split()])
