class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if (
            set(s) != set(goal) or
            len(s) != len(goal) or
            s == goal and len(s) == len(set(s))
           ):  # 79.40% 42.23%
            return False
        count = 0
        s_to = ''
        goal_to = ''
        for i in range(len(s)):
            if s[i] != goal[i]:
                count += 1
                s_to += s[i]
                goal_to += goal[i]
                if len(s_to) > 2:
                    return False
        if len(s_to) == 2:
            return set(s_to) == set(goal_to)
        return count <= 1

    def buddyStrings_best(self, s: str, goal: str) -> bool:
        if s == goal:
            if len(s) > len(set(s)):
                return True
        if len(s) != len(goal):
            return False
        if len(s) < 2 or len(goal) < 2:
            return False
        arr = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                arr.append(i)
        if len(arr) == 2:
            if s[arr[0]] == goal[arr[1]] and goal[arr[0]] == s[arr[1]]:
                return True
            else:
                return False
        else:
            return False
