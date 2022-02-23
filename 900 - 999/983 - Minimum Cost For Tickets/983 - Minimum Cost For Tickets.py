class Solution:
    def mincostTickets(self, days, costs) -> int:  # 98.29% 88.14%
        n = max(days)
        days = set(days)
        dp = [0]*(n+1)
        for i in range(1, n+1):
            if i not in days:
                dp[i] = dp[i-1]
                continue
            dp[i] = min(
                costs[0] + dp[i-1],
                costs[1] + (dp[i-7] if i-7 > 0 else 0),
                costs[2] + (dp[i-30] if i-30 > 0 else 0)
            )
        return dp[-1]

    def mincostTickets_best_speed(self, days, costs) -> int:
        # to speed up element checking for days
        travel_days = set(days)
        # ---------------------------------------------------
        # use python built-in cache as memoization for DP

        @cache
        def dp(day_d):
            # Base case
            if day_d == 0:
                # no cost on before traveling
                return 0
            # General cases
            if day_d not in travel_days:
                # no extra cost on non-traverl day
                return dp(day_d-1)
            else:
                # compute minimal cost on travel day
                with_1_day_pass = dp(day_d-1) + costs[0]
                with_7_day_pass = dp(max(day_d - 7, 0)) + costs[1]
                with_30_day_pass = dp(max(day_d - 30, 0)) + costs[2]
                return min(with_1_day_pass, with_7_day_pass, with_30_day_pass)
        last_travel_day = days[-1]
        return dp(last_travel_day)

    def mincostTickets_best_memory(self, days, costs) -> int:
        l = days[-1]+1
        dayss = set(days)
        dp = [0]*l
        for i in range(1, l):
            if i not in dayss:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[i-1]+costs[0], dp[max(i-7, 0)] +
                            costs[1], dp[max(i-30, 0)]+costs[2])
        return dp[-1]
