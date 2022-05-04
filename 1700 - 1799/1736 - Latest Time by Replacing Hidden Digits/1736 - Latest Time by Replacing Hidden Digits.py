class Solution:
    def maximumTime(self, time: str) -> str:  # 56.83% 73.74%
        hours, mins = time.split(':')
        if hours[0] == '?':
            if hours[1] != '?' and int(hours[1]) > 3:
                hours = '1' + hours[1]
            else:
                hours = '2' + hours[1]
        if hours[1] == '?':
            if hours[0] == '2':
                hours = '23'
            else:
                hours = hours[0] + '9'
        if mins[0] == '?':
            mins = '5' + mins[1]
        if mins[1] == '?':
            mins = mins[0] + '9'
        return ':'.join([hours, mins])

    def maximumTime_best_speed(self, time: str) -> str:
        t = time.split(':')
        res = []
        if t[0][0] == '?':
            if t[0][1] == '?':
                res.append('2')
                res.append('3')
            else:
                if int(t[0][1]) < 4:
                    res.append('2')
                    res.append(t[0][1])
                else:
                    res.append('1')
                    res.append(t[0][1])
        else:
            res.append(t[0][0])
            if t[0][1] == '?':
                if t[0][0] == '2':
                    res.append('3')
                else:
                    res.append('9')
            else:
                res.append(t[0][1])
        res.append(':')
        if t[1][0] == '?':
            res.append('5')
        else:
            res.append(t[1][0])
        if t[1][1] == '?':
            res.append('9')
        else:
            res.append(t[1][1])
        return ''.join(res)

    def maximumTime_best_memory(self, time: str) -> str:
        st = ''
        for i in range(len(time)):
            if time[i] == '?':
                if i == 0:
                    if time[i+1] == '?':
                        st += '2'
                    else:
                        if int(time[i+1]) < 4:
                            st += '2'
                        else:
                            st += '1'
                elif i == 1:
                    if int(st[i-1]) < 2:
                        st += '9'
                    else:
                        st += '3'
                elif i == 3:
                    st += '5'
                elif i == 4:
                    st += '9'
            else:
                st += time[i]
        return st
