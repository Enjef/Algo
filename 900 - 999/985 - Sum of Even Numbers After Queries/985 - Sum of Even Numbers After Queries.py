class Solution:
    def sumEvenAfterQueries(self, nums, queries):  # 34.47% 32.42%
        result = []
        even_sum = 0
        for num in nums:
            if not num % 2:
                even_sum += num
        for val, idx in queries:
            old = nums[idx]
            nums[idx] += val
            if nums[idx] % 2:
                if not old % 2:
                    even_sum -= old
            else:
                if old % 2:
                    even_sum += nums[idx]
                else:
                    even_sum += val
            result.append(even_sum)
        return result

    def sumEvenAfterQueries(self, nums, queries):
        even_sum = sum(num for num in nums if not num % 2)
        result = list()
        for value, index in queries:
            current = nums[index]
            new = current + value
            if not current % 2:
                even_sum -= current
            if not new % 2:
                even_sum += new
            result.append(even_sum)
            nums[index] = new
        return result

    def sumEvenAfterQueries_best_memory(self, nums, queries):
        tot = 0
        for i in nums:
            tot += i * ((i + 1) % 2)
        for i in range(len(queries)):
            tot -= nums[queries[i][1]] * ((nums[queries[i][1]] + 1) % 2)
            nums[queries[i][1]] += queries[i][0]
            tot += nums[queries[i][1]] * ((nums[queries[i][1]] + 1) % 2)
            queries[i] = tot
        return queries
