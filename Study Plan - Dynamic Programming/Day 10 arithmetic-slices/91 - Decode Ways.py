class Solution:
    def numDecodings(self, s: str) -> int:  # 78.54% 66.74%
        chars_one = {
            '1', '2', '3', '4', '5', '6', '7', '8', '9'
        }
        chars_two = {
            '10', '11', '12', '13', '14', '15', '16', '17',
            '18', '19', '20', '21', '22', '23', '24', '25', '26'
        }
        if s[0] == '0':
            return 0
        n = len(s)
        dp = [1, 1]
        for i in range(1, n):
            dp[0], dp[1] = (
                dp[1], dp[1] * (s[i] in chars_one) +
                dp[0] * (s[i-1:i+1] in chars_two))
        return dp[-1]

    def numDecodings_int(self, s: str) -> int:  # 8.52% 66.74%
        if s[0] == '0':
            return 0
        n = len(s)
        dp = [1, 1]
        for i in range(1, n):
            fail_check = 0
            fail_check = dp[1] * (int(s[i]) > 0)
            fail_check += dp[0] * (10 <= int(s[i-1:i+1]) <= 26)
            dp[0] = dp[1]
            dp[1] = fail_check
        return dp[-1]

