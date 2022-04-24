class Solution:
    def reformat(self, s: str) -> str:  # 32.00% 52.53%
        dig = []
        char = []
        for el in s:
            if el.isdigit():
                dig.append(el)
            else:
                char.append(el)
        if abs(len(dig)-len(char)) > 1:
            return ''
        res = []
        while dig and char:
            res.extend([dig.pop(), char.pop()])
        if dig:
            res.append(dig.pop())
        if char:
            res = [char.pop()] + res
        return ''.join(res)

    def reformat_best_speed(self, s: str) -> str:
        alpha_list = [ch for ch in s if ch.isalpha()]
        digit_list = [ch for ch in s if ch.isdigit()]
        len_alpha_list = len(alpha_list) 
        len_digit_list = len(digit_list)
        if abs(len_alpha_list - len_digit_list) > 1:
            return ''
        i = 0
        res_str = list()
        if len_alpha_list == len_digit_list:
            while i < len_alpha_list:
                res_str.append(alpha_list[i])
                res_str.append(digit_list[i])
                i = i + 1
        elif len_alpha_list < len_digit_list:
            while i < len_alpha_list:
                res_str.append(digit_list[i])
                res_str.append(alpha_list[i])
                i = i + 1
            res_str.append(digit_list[len_digit_list - 1])
        else:
            while i < len_digit_list:
                res_str.append(alpha_list[i])
                res_str.append(digit_list[i])
                i = i + 1
            res_str.append(alpha_list[len_alpha_list - 1])
            
        return ''.join(res_str)

    def reformat_2nd_best_speed(self, s: str) -> str:
        al = []
        num = []
        for i in s:
            if i.isnumeric():
                num.append(i)
            else:
                al.append(i)
        finalStr = ""
        if len(num) == len(al):
            for i in range(0,len(al), 1):
                finalStr += num[i] + al[i]
        elif len(num) + 1 == len(al):
            for i in range(0,len(num), 1):
                finalStr += num[i] + al[i + 1]
            finalStr = al[0] + finalStr
        elif len(num) == len(al) + 1:
            for i in range(0,len(al), 1):
                finalStr +=  al[i] + num[i + 1]
            finalStr = num[0] + finalStr
        return finalStr
