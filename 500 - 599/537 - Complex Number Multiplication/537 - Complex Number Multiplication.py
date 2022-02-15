class Solution:
    def complexNumberMultiply(self, num1, num2): # 42.18% 94.40%
        def custom_split(num):
            real, imag = 0, 0
            if '+-' in num:
                real, imag = num.split('+-')
                imag = '-' + imag
            elif '+' in num:
                real, imag = num.split('+')
            else:
                real, imag = num.split('-')
                imag = '-' + imag
            real = int(real)
            imag = int(imag[:-1])
            return real, imag
        f_real, f_imag = custom_split(num1)
        s_real, s_imag = custom_split(num2)
        return f'{f_real*s_real-f_imag*s_imag}+{f_real*s_imag+f_imag*s_real}i'

    def complexNumberMultiply_v2(self, num1, num2): # 58.70% 94.40%
        f_real, f_imag = num1.split('+')
        s_real, s_imag = num2.split('+')
        f_real, s_real = map(int, [f_real, s_real]) 
        f_imag, s_imag = map(int, [f_imag[:-1], s_imag[:-1]])
        return f'{f_real*s_real-f_imag*s_imag}+{f_real*s_imag+f_imag*s_real}i'
    
    def complexNumberMultiply_v3(self, num1, num2): # 79.35% 94.40%
        f_real, f_imag = num1.split('+')
        s_real, s_imag = num2.split('+')
        f_real = int(f_real)
        s_real = int(s_real) 
        f_imag = int(f_imag[:-1])
        s_imag = int(s_imag[:-1])
        return f'{f_real*s_real-f_imag*s_imag}+{f_real*s_imag+f_imag*s_real}i'

    def complexNumberMultiply_best_speed(self, num1: str, num2: str) -> str:
        a, bi = self.extractNums(num1)
        c, di = self.extractNums(num2)
        ac = a * c
        adi = a * di
        bic = bi * c
        bidi = bi * di * -1
        A = ac + bidi
        BI = adi + bic
        return '{}+{}i'.format(A, BI)
    def extractNums(self, num):
        values = num.split('+')
        return int(values[0]), int(values[1][:-1])


