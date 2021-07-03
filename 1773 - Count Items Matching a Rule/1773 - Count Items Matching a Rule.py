class Solution:
    def countMatches_my(self, items, ruleKey, ruleValue):  # 45.05%
        f_map = {'type': 0, 'color': 1, 'name': 2}
        count = 0
        for i in items:
            if i[f_map[ruleKey]] == ruleValue:
                count += 1
        return count

    def countMatches_best(self, items, ruleKey, ruleValue):
        if ruleKey == "type":
            idx = 0
        elif ruleKey == "color":
            idx = 1
        else:
            idx = 2
        return sum(1 for i in items if i[idx] == ruleValue)
