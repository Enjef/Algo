class Solution:
    # 22.17% 77.36% (68.87% 39.62%)
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        i = score = 0
        j = len(tokens)-1
        tokens.sort()
        while i <= j:
            if power >= tokens[i]:
                power -= tokens[i]
                score += 1
                i += 1
            elif score and i != j and tokens[i] <= power + tokens[j]:
                power += tokens[j]
                score -= 1
                j -= 1
            else:
                break
        return score

    def bagOfTokensScore_best_speed(self, tokens: List[int], power: int) -> int:
        i = 0
        j = len(tokens)-1
        score = 0
        tokens.sort()
        while i <= j:
            if tokens[i] <= power:
                score += 1
                power -= tokens[i]
                i += 1
            elif i < j and score > 0:
                score -= 1
                power += tokens[j]
                j -= 1
            else:
                break
        return score

    def bagOfTokensScore_2nd_best_speed(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        MAX = 0
        while tokens:
            if tokens[0] <= power:
                score += 1
                power -= tokens.pop(0)
                if score > MAX:
                    MAX = score
            elif score >= 1:
                power += tokens.pop()
                score -= 1
            else:
                return MAX
        return MAX

    def bagOfTokensScore_best_memory(self, tokens: List[int], power: int) -> int:
        q = deque(sorted(tokens))
        score, max_score = 0, 0
        while q:
            if power >= q[0]:
                t = q.popleft()
                power -= t
                score += 1
                max_score = max(max_score, score)
            elif score > 0:
                t = q.pop()
                score -= 1
                power += t
            else:
                break
        return max_score
