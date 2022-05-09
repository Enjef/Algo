class Solution:
    def reorderSpaces(self, text: str) -> str:  # 39.37% 71.69%
        spaces = text.count(' ')
        words = text.split()
        n = len(words)-1
        if n == 0:
            return words[0]+' '*spaces
        new_space = spaces // n
        remainder = int(spaces % n)
        return (' '*new_space).join(words) + ' '*remainder

    def reorderSpaces_best_speed(self, text: str) -> str:
        spacesNo = 0
        answer = ""
        words = text.split()
        for i in text:
            if i == " ":
                spacesNo += 1
        numberWords = len(words)
        if len(text) ==1 or numberWords == 1:
            return words[0] + " "* spacesNo
        equalnumber, remainder = divmod(spacesNo, numberWords-1)
        for i in range(numberWords):
            if i != numberWords-1:
                answer += words[i] + " " * equalnumber 
            else:
                answer += words[i]
        if remainder: answer += " "*remainder
        return answer

    def reorderSpaces_best_memory(self, text: str) -> str:
        words = [word for word in text.split(" ") if word]
        spaces = text.count(" ")
        betw = spaces // (len(words) - 1) if len(words) > 1 else spaces
        text = ""
        for i, word in enumerate(words):
            text += word + " " * betw if i != len(words) - 1 else word 
        rem = spaces - text.count(" ")
        return  text + " " * rem
