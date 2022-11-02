class Solution:
    # 63.68% 84.04%
    def decodeMessage(self, key: str, message: str) -> str:
        chars = dict()
        for char in key:
            if char != ' ' and char not in chars:
                chars[char] = chr(ord('a')+len(chars))
        res = []
        for char in message:
            if char == ' ':
                res.append(' ')
            else:
                res.append(chars[char])
        return ''.join(res)


class Solution_best_speed:
    def decodeMessage(self, key: str, message: str) -> str:
        output = ''
        list_values = []
        list_keys = []
        temp_key = key.replace(' ', '')
        key = ''
        for i in temp_key:
            if i not in key:
                key = key + i
        for i in range(len(key)):
            list_values.append(chr(i + 97))
            list_keys.append(key[i])
        mydict = {list_keys[i]: list_values[i] for i in range(len(key))}
        mydict.update({' ': ' '})
        for item in message:
            output += mydict[item]
        return output


class Solution_best_memory:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {}
        k = 97
        for i in key:
            if i != ' ' and i not in d:
                d[i] = chr(k)
                k += 1
        res = ''
        for i in message:
            if i != ' ':
                res += d[i]
            else:
                res += ' '
        return res
