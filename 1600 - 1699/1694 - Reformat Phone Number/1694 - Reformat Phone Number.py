class Solution:
    def reformatNumber(self, number: str) -> str:  # 9.90% 17.17%
        nums = [str(x) for x in number if x.isdigit()]
        if len(nums) == 2:
            return ''.join(nums)
        if len(nums) % 3 == 0:
            return '-'.join(
                [''.join(nums[i:i+3]) for i in range(0, len(nums), 3)]
            )
        if len(nums) % 3 == 1:
            temp = [''.join(nums[i:i+3]) for i in range(0, len(nums)-4, 3)]
            temp.extend([''.join(nums[-4:-2]), ''.join(nums[-2:])])
            return '-'.join(temp)
        if len(nums) % 3 == 2:
            temp = [''.join(nums[i:i+3]) for i in range(0, len(nums)-2, 3)]
            temp.append(''.join(nums[-2:]))
            return '-'.join(temp)
        return number

    def reformatNumber_best_speed(self, number: str) -> str:
        number = number.replace('-', '')
        number = number.replace(' ', '')
        s = ''
        while(len(number) > 0):
            i = len(number)
            if i <= 3:
                s = s + number + '-'
                number = ''
            elif i > 4:
                s = s + number[:3] + '-'
                number = number[3:]
            else:
                s = s + number[:2] + '-'
                number = number[2:]
        if s[-1] == '-':
            return s[:-1]
        else:
            return s

    def reformatNumber_best_memory(self, number: str) -> str:
        number = number.replace(" ", "").replace("-", "")
        i = 0
        output = []
        while i < len(number):
            if len(number)-i == 4:
                output.append(number[i:i+2])
                i += 2
            elif len(number)-i >= 3:
                output.append(number[i:i+3])
                i += 3
            else:
                output.append(number[i:i+2])
                i += 2
        return "-".join(output)
