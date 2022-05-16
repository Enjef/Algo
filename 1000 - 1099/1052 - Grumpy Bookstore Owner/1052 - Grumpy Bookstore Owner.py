class Solution:
    def maxSatisfied(self, customers, grumpy, minutes):  # 53.83% 85.65%
        n = len(customers)
        total = 0 
        for i in range(n):
            total += customers[i] * int(not(grumpy[i]))
        cur_sum = total + sum(
            [customers[i] for i in range(minutes) if grumpy[i]])
        result = cur_sum
        for i in range(minutes, n):
            if grumpy[i]:
                cur_sum += customers[i]
            if grumpy[i-minutes]:
                cur_sum -= customers[i-minutes]
            result = max(result, cur_sum)
        return result  

    def maxSatisfied_best_speed(self, customers, grumpy, minutes):
        notGrumpy = 0
        isGrumpy = 0
        maxGrumpy = 0
        pointer1 = 0
        for index in range(0, len(customers)):
            if index >= minutes:
                if grumpy[pointer1]:
                    isGrumpy -= customers[pointer1]
                pointer1 += 1
            if grumpy[index] == 0:
                notGrumpy += customers[index]
            else:
                isGrumpy = isGrumpy + customers[index]
                if isGrumpy > maxGrumpy:
                    maxGrumpy = isGrumpy
        return maxGrumpy + notGrumpy

    def maxSatisfied_best_memory(self, customers, grumpy, minutes):
        satisfied = 0
        unsatisfiedSum = 0
        unsatisfied = Queue()
        prevSum = 0
        for i, c in enumerate(customers):
            if not grumpy[i]:
                satisfied += c
            popped = 0
            if i >= minutes:
                popped = unsatisfied.get()
            newItem = c if grumpy[i] else 0
            newSum = prevSum - popped + newItem
            prevSum = newSum
            unsatisfied.put(newItem)
            unsatisfiedSum = max(unsatisfiedSum, newSum)
        return satisfied + unsatisfiedSum
