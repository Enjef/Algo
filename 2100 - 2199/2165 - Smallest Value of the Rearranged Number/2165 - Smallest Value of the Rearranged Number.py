class Solution:
    def smallestNumber(self, num: int) -> int:  # 43.55% 20.28%
        negative = False
        if num < 0:
            negative = True
        new = sorted(
            str(num)[1:] if negative else str(num), reverse=negative)
        if new[0] == '0':
            for i in range(1, len(new)):
                if new[i] != '0':
                    new[0], new[i] = new[i], new[0]
                    break
        new = int(''.join(new))
        return -new if negative else new

    def smallestNumber_best_speed(self, num: int) -> int:
        # zero case
        if num == 0:
            return 0
        # int -> string
        str_num = str(num)
        num_list = []
        # string -> list
        num_list[:0] = str_num
        # positive case
        if num > 0:
            # sort accending
            num_list.sort()
            # if 0 is leading
            if num_list[0] == '0':
                zero = True
                index = 0
                # count how many zeros
                while zero == True:
                    index += 1
                    if num_list[index] != '0':
                        zero = False
                # replace first int after 0 as first index
                num_list[0] = num_list[index]
                # replace int index with 0
                num_list[index] = '0'
            # list -> string -> int -> return
            return int(''.join(num_list))
        # negative case
        else:
            # sort decending
            num_list.sort(reverse=True)
            # get rid of the '-' at the end of lsit
            num_list = num_list[:-1]
            # list -> string
            num_str = ''.join(num_list)
            # add back on the '-'
            num_str = '-' + num_str
            # string -> int -> return
            return int(num_str)

    def smallestNumber_2nd_best_speed(self, num: int) -> int:
        if num == 0:
            return 0
        s = ''
        if num < 0:
            s = '-'+''.join(sorted(str(num)[1:])[::-1])
        else:
            s = ''.join(sorted(str(num)))
            if '0' in s:
                c = s.count('0')
                if len(s) >= c+2:
                    s = s[c]+'0'*c+s[c+1:]
                else:
                    s = s[c]+'0'*c
        return s

    def smallestNumber_best_memory(self, num: int) -> int:
        k = str(num)
        m = []
        for i in range(len(k)):
            if k[i].isnumeric():
                m.append(k[i])
        if num >= 0:
            m.sort()
            if m[0] == '0':
                for i in range(len(m)):
                    if m[i] != '0':
                        m[i], m[0] = m[0], m[i]
                        break
                string1 = ''.join(map(str, m))
                return string1
            else:
                string1 = ''.join(map(str, m))
                return string1
        else:
            m.sort(reverse=True)
            string1 = ''.join(map(str, m))
            k = -int(string1)
            return k
