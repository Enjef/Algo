class Solution(object):
    def checkIfPangram(self, sentence):  # 36%
        abc_set = set('abcdefghijklmnopqrstuvwxyz')
        sentence = set(sentence)
        return abc_set == sentence

    def top_four(self, sentence):
        return len(set(sentence)) == 26
