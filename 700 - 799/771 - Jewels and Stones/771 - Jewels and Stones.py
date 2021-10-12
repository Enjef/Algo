class Solution(object):
    def numJewelsInStones_my(self, jewels, stones):
        count = 0
        for jewel in jewels:
            count += stones.count(jewel)
        return count

    def numJewelsInStones_better(self, jewels, stones):
        output = 0
        storage = set()

        for i in jewels:
            if i not in storage:
                storage.add(i)

        for j in stones:
            if j in storage:
                output += 1

        return output
